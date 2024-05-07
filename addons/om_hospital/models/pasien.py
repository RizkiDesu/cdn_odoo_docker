from odoo import api, fields, models
from datetime import date

class CdnPasien(models.Model):
    _name           = 'cdn.pasien'
    _description    = 'Cdn Pasien'
    _inherit        = ['mail.thread','mail.activity.mixin']
    

    name            = fields.Char(string='Nama Pasien', tracking=True)
    tgl_lahir       = fields.Date(string='Tangggal Lahir')
    ref             = fields.Char(string='Refrensi', default='Odoo Mates')

    umur            = fields.Integer(string='Umur', tracking=True, compute='_compute_umur')
    
    @api.depends('tgl_lahir')
    def _compute_umur(self):
        for rec in self:
            today = date.today()
            if rec.tgl_lahir:
                rec.umur = today.year - rec.tgl_lahir.year
            else:
                rec.umur = 0 #jika tidak di kasih else nilai bakal null dan error
    
    jenis_kel       = fields.Selection(string='Jenis Kelamin', 
                                 selection=[('l', 'laki laki'), 
                                            ('p', 'perempuan'),], 
                                            tracking=True,
                                            default='p')
    
    active          = fields.Boolean(string='Aktif', default=True) #spesial 

    appoinment_id   = fields.Many2one(comodel_name='cdn.appointment', string='Pasien')
    image           = fields.Image(string='gambar')
    tag_ids         = fields.Many2many(comodel_name='cdn.pasien.tag', string='Tags')
    
    
    

    
    
    



    
