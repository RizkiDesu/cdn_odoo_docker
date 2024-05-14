from odoo import models, fields, api

from datetime import date

class DsAnggota(models.Model):
    _name = 'ds.anggota'
    _description = 'Ds Anggota'

    name = fields.Char(string='Nama Anggota')

    jenis_kelamin = fields.Selection(string='Jenis Kelmin', selection=[('l', 'Laki-laki'), ('p', 'Perempuan'),])

    nomor_anggota = fields.Char(string='Nomor Anggota')
    pejabat_id = fields.Many2one(comodel_name='desu.pejabat', string='Nama Atasan')
    
    jabatan_pejabat = fields.Char(string='Jabatan Atasan', store=True, readonly=True)
    @api.onchange('pejabat_id')
    def _onchange_pasien_id(self):
        # self.jabatan_pejabat = self.pejabat_id.jenis_jabatan
        # print('jenis_jabatan ATASAN', self.pejabat_id.jenis_jabatan)
        # jenis_jabatan ATASAN staf
        # jenis_jabatan ATASAN wakil
        # jenis_jabatan ATASAN False
        # jenis_jabatan ATASAN staf
        # jenis_jabatan ATASAN False
        if self.pejabat_id not in [False, None]: #
            self.jabatan_pejabat = self.pejabat_id.jenis_jabatan
        else:
            self.jabatan_pejabat = 'atasan tidak menjabat jabatan apapun'


    # umur dan tanggal lahir
    tanggal_lahir = fields.Date(string='Tanggal Lahir')
    umur = fields.Integer(string='Umur', compute='_hitung_umur_dari_lahir', store=True)
    @api.depends('tanggal_lahir')
    def _hitung_umur_dari_lahir(self):
        for rec in self:
            today = date.today()
            if rec.tanggal_lahir:
                rec.umur = today.year - rec.tanggal_lahir.year
            else:
                rec.umur = 0