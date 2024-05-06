from odoo import api, fields, models

class CdnAppointment(models.Model):
    _name           = 'cdn.appointment'
    _description    = 'Cdn Appointment'
    _rec_name       = 'ref' # record efeknya akan menampikalan nama buakn id


    pasien_id       = fields.Many2one(comodel_name='cdn.pasien', string='Pasien')
    appoinment_time = fields.Datetime(string='Appoinment Time', default=fields.Datetime.now)
    jenis_kel       = fields.Selection(related='pasien_id.jenis_kel')
    booking_date    = fields.Date(string='Tanggal Booking', default=fields.Date.context_today)
    ref             = fields.Char(string='Refrensi')

    @api.onchange('pasien_id')
    def _onchange_pasien_id(self):
        self.ref = self.pasien_id.ref
    
    
    
