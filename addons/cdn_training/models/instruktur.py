from odoo import models, fields, api

class Instruktur(models.Model):
    _name           = 'instruktur'
    _description    = 'Instruktur'
    _inherits       = {'res.partner' : 'partner_id'}

    partner_id      = fields.Many2one(comodel_name='res.partner', string='Partner ID',ondelete='cascade', required=True)
    keahlian_ids    = fields.Many2many(comodel_name='keahlian', string='Keahlian')

class Keahlian(models.Model):
    _name           = 'keahlian'
    _description    = 'Keahlian'
    name            = fields.Char(string='Nama Keahlian', required=True)