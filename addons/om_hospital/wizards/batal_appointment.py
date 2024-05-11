from odoo import api, fields, models
import datetime as tanggal

class CdnWzBatalapointment(models.TransientModel):
    _name           = 'cdn.wz.batalapointment'
    _description    = 'Cdn Wz Batalapointment'

    appointment_id  = fields.Many2one(comodel_name='cdn.pasien', string='Appointment')

    reason          = fields.Text(string='Reason') 
    tanggal_batal = fields.Date(string='Tanggal Batal')
    
    
    @api.model
    def default_get(self, fields): # fungsi default get untuk mengisi tanggal batal dengan tanggal hari ini
        ref = super (CdnWzBatalapointment, self).default_get(fields) # mengisi ref dengan default get
        # print("default get executed", ref) # print untuk mengecek apakah default get sudah terbaca atau belum
        ref['tanggal_batal'] = tanggal.date.today() # mengisi tanggal batal dengan tanggal hari ini
        # ref['tanggal_batal'] = fields.Date.context_today(self) # ora iso
        return ref
    
    def action_cancel(self): # fungsi cancel untuk mengubah state menjadi cancel
        return # mengembalikan action
    