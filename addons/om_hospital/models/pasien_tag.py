from odoo import api, fields, models


class CdnPasienTag(models.Model):
    _name           = 'cdn.pasien.tag' # Model name
    _description    = 'Cdn Pasien Tag' # Model description

    name            = fields.Char(string='Nama Tag', required=True)  # field name
    active          = fields.Boolean(string='Aktif', default=True) # field active
    warna           = fields.Integer(string='Warna') # field warna
    warna2          = fields.Char(string='Warna 2') # field warna 2
    