from odoo import models, fields, api



class DesuHitung(models.Model):
    _name = 'desu.hitung'
    _description = 'Desu Hitung'

    name = fields.Char(string='Hitung')

    kelipatan = fields.Integer(string='angka1')
    hasil = fields.Integer(string='Hasil 2x lipat', compute='_2xlipat', store=True)
    @api.depends('kelipatan')
    def _2xlipat(self):
        self.hasil=self.kelipatan * self.kelipatan