from odoo import api, fields, models


class CdnPasien(models.Model):
    _name = 'cdn.pasien'
    _description = 'Cdn Pasien'

    name = fields.Char(string='Nama Pasien')
    ref = fields.Char(string='Refrensi')
    umur = fields.Integer(string='Umur')
    jenis_kel = fields.Selection(string='Jenis Kelamin', 
                                 selection=[('l', 'laki laki'), 
                                            ('p', 'perempuan'),])
    active = fields.Boolean(string='Aktif', default=True)
    

    
    
    



    
