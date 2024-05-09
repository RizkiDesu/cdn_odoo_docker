from odoo import fields, api, models



class SaleOlder(models.Model):
    _inherit = 'sale.order'

    konfirmasi_user_id = fields.Many2one(comodel_name='res.users', string='Konfirmasi Akun')
    