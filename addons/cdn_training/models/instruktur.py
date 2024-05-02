from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Instruktur(models.Model):
    _name           = 'instruktur'
    _description    = 'Instruktur'
    _inherits       = {'res.partner' : 'partner_id'}

    partner_id      = fields.Many2one(comodel_name='res.partner', string='Partner ID',ondelete='cascade', required=True)
    keahlian_ids    = fields.Many2many(comodel_name='keahlian', string='Keahlian')

    jabatan_id      = fields.Many2one(comodel_name='dn.jabatan', string='Jabatan', ondelete='cascade')
    jenis_jabatan   = fields.Selection(related='jabatan_id.jenis_jabatan', readonly=False)
    jabatan_staff  = fields.Char(string="Jabatan Staff")
    # _sql_constraints    = [
    #     ("unique_jabatan_id_kepala", "UNIQUE(jabatan_id)", "Hanya boleh 1 kepala"),
    #     ("unique_jabatan_id_wakil", "UNIQUE(jabatan_id)", "Hanya boleh 1 Wakil kepala"),
    # ]

    

    # @api.constrains('jabatan_id')
    # def _constrains_unique_dn_jabatan_id(self):
    #     for rec in self:
    #         if rec.jabatan_id.jenis_jabatan in ['kepala','wakil']:
    #             record = self.search([('jabatan_id', '=', rec.jabatan_id.id)])
    #             if len(record) > 1 :
    #                 raise ValidationError("hanya boleh dapat 1 jabatan saja {}.".format(rec.jabatan_id.jenis_jabatan.capitalize()))
        
    def update(self):
        self.jabatan_id.pejabat_id = self.id
        return True
        

    
class Keahlian(models.Model):
    _name           = 'keahlian'
    _description    = 'Keahlian'
    name            = fields.Char(string='Nama Keahlian', required=True)


class DnJabatan(models.Model):
    _name           = 'dn.jabatan'
    _description    = 'Dn Jabatan'

    name            = fields.Char(string='Nama jabatan', ondelete='cascade')
    jenis_jabatan   = fields.Selection(string='Jenis Jabatan', 
                                       selection=[('kepala', 'Kepala / Pimpinan Lembaga'), 
                                                  ('wakil', 'Wakil Kepala Lembaga'),
                                                  ('staf','Staff')])
    keterangan      = fields.Text(string='Keterangan')

    pejabat_id      = fields.Many2one(comodel_name='instruktur', string='Pejabat')

    # _sql_constraints    = [
    #     ("unique_kepala", "UNIQUE(jenis_jabatan)", "Hanya boleh 1 kepala"),
    #     ("unique_wakil", "UNIQUE(jenis_jabatan)", "Hanya boleh 1 Wakil kepala")
    # ]
    
    def pejabat(selft):
        print(selft.pejabat_id)


    
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