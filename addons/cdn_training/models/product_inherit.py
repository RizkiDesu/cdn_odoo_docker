from odoo import models, fields, api



# omomdi
class ProductProduct(models.Model):
    _inherit = 'product.product'

    produk_pelatihan = fields.Selection(string='Jenis Prduk Training', 
                                        selection=[('non_training', 'Non Produk Training'), 
                                                   ('kosumsi', 'Kosumsi Training'),
                                                   ('training_Kit','Peralatan Training')], 
                                                   default='non_training')
    
    

