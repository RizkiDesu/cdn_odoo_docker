from odoo import models, fields, api

class CdnDokter(models.Model):
    _name           = 'cdn.dokter'
    _description    = 'Dokter'
    _inherits       = {'res.partner' : 'partner_id'}

    partner_id      = fields.Many2one(comodel_name='res.partner', string='Partner ID',ondelete='cascade')
    spesialis_ids    = fields.Many2many(comodel_name='cdn.spesialis', string='Sepesialis')


class CdnSpesialis(models.Model):
    _name           = 'cdn.spesialis'
    _description    = 'Spesialis'

    name            = fields.Char(string='Sepesialis')

    