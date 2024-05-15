from odoo import api, fields, models,_



class CdnOprasional(models.Model):
    _name = 'cdn.oprasional'
    _description = 'Cdn Oprasional'
    _log_access = False # disable log access berfungsi untuk menghilangkan log access pada tabel sehingga tidak ada history log

    doctor_id = fields.Many2one(comodel_name='res.users', string='Doctor')
    operasional_name = fields.Char(string='Name')

    # fungsi name get untuk mengambil nama di view model lain
    @api.model
    def name_create(self, name):
        print("name_create", name)
        return self.create({'operasional_name': name}).name_get()[0] 