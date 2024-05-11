from odoo import fields, api, models # meimport class fields, api, dan models dari module odoo

class SaleOlder(models.Model): 
    _inherit = 'sale.order'  # mendeklarasikan model yang diinherit adalah 'sale.order'

    konfirmasi_user_id = fields.Many2one(comodel_name='res.users', string='Konfirmasi Akun')  # mendeklarasikan field konfirmasi_user_id dengan tipe data many2one yang merujuk pada model 'res.users' dan string 'Konfirmasi Akun'

    def action_confirm(self):
        
        super(SaleOlder, self).action_confirm()  # memanggil method action_confirm dari class parent
        print("sukses.......................")
        self.konfirmasi_user_id = self.env.user.id # mengisi field konfirmasi_user_id dengan id user yang sedang login
    