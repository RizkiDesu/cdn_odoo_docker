from odoo import api, fields, models

class CdnAppointment(models.Model):
    _name = 'cdn.appointment'
    _description = 'Cdn Appointment'


    pasien_id = fields.Many2one(comodel_name='cdn.pasien', string='Pasien')
    appoinment_time = fields.Datetime(string='Appoinment Time', default=fields.Datetime.now)
    
    booking_date = fields.Date(string='Tanggal Booking', default=fields.Date.context_today)
    
    
    
