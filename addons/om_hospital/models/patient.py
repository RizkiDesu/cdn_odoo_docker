from odoo import api, fields, models


class CdnPasien(models.Model):
    _name = 'cdn.pasien'
    _description = 'Cdn Pasien'
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string='Nama Pasien', tracking=True)
    ref = fields.Char(string='Refrensi')
    umur = fields.Integer(string='Umur', tracking=True)
    jenis_kel = fields.Selection(string='Jenis Kelamin', 
                                 selection=[('l', 'laki laki'), 
                                            ('p', 'perempuan'),], tracking=True)
    active = fields.Boolean(string='Aktif', default=True)
    

    
    
    



    
