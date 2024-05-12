from odoo import api, fields, models
import datetime as tanggal

class CdnWzBatalapointment(models.TransientModel):
    _name           = 'cdn.wz.batalapointment'
    _description    = 'Cdn Wz Batalapointment'

    # appointment_id  = fields.Many2one(comodel_name='cdn.pasien', string='Appointment') #keliruu harusnya cdn.appointment
    app_id = fields.Many2one(comodel_name='cdn.appointment', string='Janji Konsultasi')
    

    reason          = fields.Text(string='Reason') 
    tanggal_batal   = fields.Date(string='Tanggal Batal')
    
    
    @api.model
    def default_get(self, fields): 
        ref = super (CdnWzBatalapointment, self).default_get(fields)
        ref['tanggal_batal'] = tanggal.date.today() 
        ref['reason'] = 'Alasan Batal'
        # print("............", self.env.context) # hasil ............{'lang': 'en_US', 'tz': 'Asia/Jakarta', 'uid': 2, 'allowed_company_ids': [1], 'active_model': 'cdn.appointment', 'active_id': 24, 'active_ids': [24]}
        if self.env.context.get('active_id'): # jika active id ada
            ref['app_id'] = self.env.context.get('active_id') # mengambil active id
        return ref
    
    def action_cancel(self): # fungsi cancel untuk mengubah state menjadi cancel
        return # mengembalikan action
    