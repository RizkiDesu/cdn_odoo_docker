from odoo import api, fields, models

class CdnAppointment(models.Model):
    _name = 'cdn.appointment'
    _description = 'Cdn Appointment'

    pasien_id = fields.Many2one(comodel_name='cdn.pasien', string='Pasien')
    
