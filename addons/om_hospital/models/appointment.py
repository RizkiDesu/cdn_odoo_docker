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
    keadaan         = fields.Selection([
                                ('draf', 'Draft'),
                                ('on_consultasion', 'Lagi Konsultasi'),
                                ('done', 'Selesai'),
                                ('cancel', 'Batal')
                                ], string="Keadaan", required=True, default='draf')
    dokter_id          = fields.Many2one(comodel_name='res.users', string='Dokter')
    

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
    
    
    
