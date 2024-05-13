from odoo import fields, models


class ResConfigSettings(models.TransientModel): # transien model adalah model yang tidak di simpan di database
    _inherit = 'res.config.settings'

    hari_batal = fields.Integer(string='Hari Batal', config_parameter='om_hospital.hari_batal') # field hari batal dengan tipe integer
