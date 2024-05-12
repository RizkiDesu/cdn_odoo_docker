from odoo import api, fields, models


class CdnPasienTag(models.Model):
    _name           = 'cdn.pasien.tag' # Model name
    _description    = 'Cdn Pasien Tag' # Model description

    name            = fields.Char(string='Nama Tag', required=True)  # field name
    active          = fields.Boolean(string='Aktif', default=True) # field active
    warna           = fields.Integer(string='Warna') # field warna
    warna2          = fields.Char(string='Warna 2') # field warna 2
    sequence        = fields.Integer(string='Sequence') # field sequence

    _sql_constraints = [ # constraint
        # ('unique_tag_name', 'unique(name, active)', 'Nama Harus Unik'), 
        ('unique_tag_name', 'unique(name)', 'Nama Harus Unik'), 
        ('chek_sequence', 'check(sequence > 0)', 'Sequence tidak boleh angka dibawah 0') 
    ]

    # _sql_constraints    = [
    #     ("name_course_unique", "UNIQUE(name)", "Nama Kursus Sudah Ada"),
    # ]
    