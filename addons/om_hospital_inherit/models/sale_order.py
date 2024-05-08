from odoo import api, fields, models



class CdnSaleOlder(models.Model):
    # _name = 'cdn.sale.older'
    # _description = 'Cdn Sale Older'
    _inherit = 'sale.order'

    name = fields.Char(string='Nama', required=True)

    def test(self):
        return
    
