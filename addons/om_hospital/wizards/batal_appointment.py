from odoo import api, fields, models


class CdnWzBatalapointment(models.TransientModel):
    _name = 'cdn.wz.batalapointment'
    _description = 'Cdn Wz Batalapointment'

    appointment_id = fields.Many2one(comodel_name='cdn.pasien', string='Appointment')

    def action_cancel(self):
        return
    