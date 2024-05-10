from odoo import fields, api, models # Import the fields, api, and models modules from Odoo.

class SaleOlder(models.Model): # Create a new class for the sale order model.
    _inherit = 'sale.order' # Inherit the sale.order model to add new fields.

    konfirmasi_user_id = fields.Many2one(comodel_name='res.users', string='Konfirmasi Akun') # Field to store the user who confirmed the sale order.
    