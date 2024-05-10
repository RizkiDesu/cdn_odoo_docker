from odoo import models, fields, api



class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    produk_pelatihan = fields.Selection(string='Jenis Prduk Training', 
                                        selection=[('non_training', 'Non Produk Training'), 
                                                   ('kosumsi', 'Kosumsi Training'),
                                                   ('training_Kit','Peralatan Training')], 
                                                   default='non_training')
    
    