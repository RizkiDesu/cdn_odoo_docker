from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Instruktur(models.Model):
    _name           = 'instruktur'
    _description    = 'Instruktur'
    _inherits       = {'res.partner' : 'partner_id'}

    partner_id      = fields.Many2one(comodel_name='res.partner', string='Partner ID',ondelete='cascade', required=True)
    keahlian_ids    = fields.Many2many(comodel_name='keahlian', string='Keahlian')

    jabatan_id      = fields.Many2one(comodel_name='dn.jabatan', )
    jenis_jabatan   = fields.Selection(string='Jenis Jabatan', related='jabatan_id.jenis_jabatan', readonly=False)


class Keahlian(models.Model):
    _name           = 'keahlian'
    _description    = 'Keahlian'
    name            = fields.Char(string='Nama Keahlian', required=True)

class DnJabatan(models.Model):
    _name           = 'dn.jabatan'
    _description    = 'Dn Jabatan'

    name            = fields.Char(string='Nama jabatan')
    jenis_jabatan   = fields.Selection(string='Jenis Jabatan', selection=[('kepala', 'Kepala / Pimpinan Lembaga'), ('wakil', 'Wakil Kepala Lembaga'),('staf','Staff')])
    keterangan      = fields.Text(string='Keterangan')


    pejabat_id      = fields.Many2one(comodel_name='instruktur', string='Nama Pejabat', readonly=True)
    nama_pejabat    = fields.Char(string='Nama Instruktur', related='pejabat_id.partner_id.name', store=True)

    
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