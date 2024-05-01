from odoo import models, fields, api
from odoo.exceptions import ValidationError


class DesuJabatan(models.Model):
    _name = 'desu.jabatan'
    _description = 'DesuJabatan'

    name            = fields.Char(string='Nama Jabatan')
    jenis_jabatan   = fields.Selection(
                            string='Jenis Jabatan', 
                            selection=[('kepala', 'Kepala / Pimpinan Lembaga'), 
                                        ('wakil', 'Wakil Kepala Lembaga'),
                                        ('staf','Staff')], readonly=True)
    
    pejabat_ids     = fields.One2many(comodel_name='desu.pejabat',  
                                      inverse_name='jabatan_id', 
                                      string='Pejabat')
    
    @api.constrains('jenis_jabatan')
    def _check_jenis_jabatan_limit(self):
        for rec in self:
            if rec.jenis_jabatan == 'kepala':
                count = self.search_count([('jenis_jabatan', '=', 'kepala')])
                if count > 1:
                    raise ValidationError("Kepala/Pimpinan Lembaga Hanya 1 yang di izinkan")
            if rec.jenis_jabatan == 'wakil':
                count = self.search_count([('jenis_jabatan', '=', 'wakil')])
                if count > 1:
                    raise ValidationError("Wakil Kepala Lembaga Hanya 1 yang di izinkan")

    
