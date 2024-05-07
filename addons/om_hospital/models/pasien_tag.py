from odoo import api, fields, models


class CdnPasienTag(models.Model):
    _name           = 'cdn.pasien.tag'
    _description    = 'Cdn Pasien Tag'

    name            = fields.Char(string='Nama Tag', required=True)
    active          = fields.Boolean(string='Aktif', default=True)
    warna           = fields.Integer(string='Warna')
    warna2          = fields.Char(string='Warna 2')
    