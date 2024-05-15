from odoo import api, fields, models,_



class CdnOprasional(models.Model):
    _name = 'cdn.oprasional'
    _description = 'Cdn Oprasional'
    _log_access = False # disable log access berfungsi untuk menghilangkan log access pada tabel sehingga tidak ada history log

    doctor_id = fields.Many2one(comodel_name='res.users', string='Doctor')

