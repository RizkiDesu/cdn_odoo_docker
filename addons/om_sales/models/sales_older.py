from odoo import fields, api, models



class CdnSalesOlder(models.Model):
    _inherit = 'sales.older' # mewarisi dari sales app awaan odoo

    comfirrmed_user_id = fields.Many2one(comodel_name='res.users', string='Confirmed User') # 

    
