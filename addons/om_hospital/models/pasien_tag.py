from odoo import api, fields, models,_


class CdnPasienTag(models.Model):
    _name           = 'cdn.pasien.tag' # Model name
    _description    = 'Cdn Pasien Tag' # Model description

    name            = fields.Char(string='Nama Tag', required=True)  # field name
    active          = fields.Boolean(string='Aktif', default=True) # field active
    warna           = fields.Integer(string='Warna') # field warna
    warna2          = fields.Char(string='Warna 2') # field warna 2
    sequence        = fields.Integer(string='Sequence', default=1) # field sequence

    @api.returns('self', lambda value: value.id) # fungsi untuk mengembalikan nilai id
    def copy(self, default=None): # fungsi untuk mengcopy data
        if default is None: # jika default kosong
            default = {} # default di isi dengan dictionary kosong
        if not default.get('name'): # jika tidak ada nama
            default['name'] = _("%s (copy)") % (self.name) # nama di isi dengan nama copy
        default['sequence'] = 10
        return super(CdnPasienTag, self).copy(default) # copy data
    
    _sql_constraints = [ # constraint
        # ('unique_tag_name', 'unique(name, active)', 'Nama Harus Unik'), 
        ('unique_tag_name', 'unique(name)', 'Nama Harus Unik'), 
        ('chek_sequence', 'check(sequence > 0)', 'Sequence tidak boleh angka dibawah 0') 
    ]
    