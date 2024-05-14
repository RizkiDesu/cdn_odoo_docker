from odoo import models, fields, api

class DesuPejabat(models.Model):
    _name = 'desu.pejabat'
    _description = 'Desu Pejabat'

    name = fields.Char(string='Nama')

    jenis_jabatan = fields.Selection(related='jabatan_id.jenis_jabatan', readonly=False, store=True)
    
    jabatan_id = fields.Many2one(comodel_name='desu.jabatan', string='Jabatan')
    
    jabatan_staff = fields.Char(string='Staff')

    anggota_ids = fields.One2many(comodel_name='ds.anggota', inverse_name='pejabat_id', string='Anggota')

    @api.onchange('jenis_jabatan')
    def _onchange_jabatan_id(self):
        self.jabatan_id.jenis_jabatan = self.jenis_jabatan
    
    
