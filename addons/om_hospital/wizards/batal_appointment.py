from odoo import api, fields, models
import datetime as tanggal

class CdnWzBatalapointment(models.TransientModel):
    _name           = 'cdn.wz.batalapointment'
    _description    = 'Cdn Wz Batalapointment'

    appointment_id  = fields.Many2one(comodel_name='cdn.pasien', string='Appointment')

    reason          = fields.Text(string='Reason') 
    tanggal_batal = fields.Date(string='Tanggal Batal')
    
    
    @api.model
    def default_get(self, fields):
        ref = super (CdnWzBatalapointment, self).default_get(fields)
        print("default get executed", ref)
        ref['tanggal_batal'] = tanggal.date.today()
        # ref['tanggal_batal'] = fields.Date.context_today(self) # ora iso
        return ref
    
    def action_cancel(self):
        return
    