from odoo import models, fields, api

class DesuPejabat(models.Model):
    _name = 'desu.pejabat'
    _description = 'Desu Pejabat'

    name = fields.Char(string='Nama')

    jenis_jabatan = fields.Selection(related='jabatan_id.jenis_jabatan', readonly=False)
    
    jabatan_id = fields.Many2one('desu.jabatan', string='Jabatan')
    # jabatan_ids = fields.One2many(comodel_name='desu.jabatan', inverse_name='pejabat_id', string='')
    

    @api.onchange('jenis_jabatan')
    def _onchange_jabatan_id(self):
        self.jabatan_id.jenis_jabatan = self.jenis_jabatan
    
    
