from odoo import api, fields, models

class CdnAppointment(models.Model):
    _name           = 'cdn.appointment'
    _inherit        = ['mail.thread','mail.activity.mixin']
    _description    = 'Cdn Appointment'
    _rec_name       = 'ref' # record efeknya akan menampikalan nama buakn id


    pasien_id       = fields.Many2one(comodel_name='cdn.pasien', string='Pasien')
    appoinment_time = fields.Datetime(string='Appoinment Time', default=fields.Datetime.now)
    jenis_kel       = fields.Selection(related='pasien_id.jenis_kel')
    booking_date    = fields.Date(string='Tanggal Booking', default=fields.Date.context_today)
    ref             = fields.Char(string='Refrensi', help="refrenis ke pasien record")
    resep           = fields.Html(string='Resep')
    ploritas        = fields.Selection([
                                ('0', 'Normal'),
                                ('1', 'Low'),
                                ('2', 'High'),
                                ('3', 'Very High')
                                # ('4', 'God')
                                ], string="Priority") # jumlah bintang mengikuti ini
    state           = fields.Selection([
                                ('draf', 'Draft'),
                                ('on_consultasion', 'Lagi Konsultasi'),
                                ('done', 'Selesai'),
                                ('cancel', 'Batal')
                                ], string="Keadaan", required=True, default='draf') #state spesial
    dokter_id       = fields.Many2one(comodel_name='res.users', string='Dokter', Tracking=True)

    farmasi_ids     = fields.One2many(comodel_name='cdn.farmasi', inverse_name='appointment_id', string='Farmasi')
    
    sembunyi_sales_harga = fields.Boolean(string='Sembuyikan Sales Harga')
    

    @api.onchange('pasien_id')
    def _onchange_pasien_id(self):
        self.ref = self.pasien_id.ref
    
    def action_test(self):
        print("button test !!!")
        return {
                'effect': {
                    'fadeout': 'slow',
                    'message': 'Berhasil di klik',
                    'type': 'rainbow_man',
                }
            }
    def action_on_consultasion(self):
        for rec in self:
            rec.state ='on_consultasion'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'
    def action_draf(self):
        for rec in self:
            rec.state = 'draf'

class CdnFarmasi(models.Model):
    _name           = 'cdn.farmasi'
    _description    = 'Cdn Farmasi'

    produk_id       = fields.Many2one(comodel_name='product.product', required=True) #tambahkan product di manifest
    harga_unit      = fields.Float(string='Harga',related='produk_id.list_price')
    qty             = fields.Integer(string='Quantity', default=1)
    appointment_id  = fields.Many2one(comodel_name='cdn.appointment', string='Appointment')
    