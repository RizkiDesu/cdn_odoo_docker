from odoo import api, fields, models,_
from datetime import date
from odoo.exceptions import ValidationError as pesan_error

class CdnPasien(models.Model):
    _name           = 'cdn.pasien' # nama tabel di database
    _description    = 'Cdn Pasien' # deskripsi tabel di database
    _inherit        = ['mail.thread','mail.activity.mixin'] # tambahkan mail thread untuk mengirim email
    

    name            = fields.Char(string='Nama Pasien', tracking=True) # field nama pasien
    tgl_lahir       = fields.Date(string='Tangggal Lahir') # field tanggal lahir
    # ref             = fields.Char(string='Refrensi', default='Odoo Mates') # field refrensi dengan nilai default Odoo Mates
    ref             = fields.Char(string='Refrensi') # field refrensi 

    umur            = fields.Integer(string='Umur', tracking=True, compute='_compute_umur')  # field umur dengan fungsi compute _compute_umur untuk menghitung umur pasien berdasarkan tanggal lahir pasien
    
    jenis_kel       = fields.Selection(string='Jenis Kelamin', 
                                 selection=[('l', 'laki laki'), 
                                            ('p', 'perempuan'),], 
                                            tracking=True,
                                            default='p') 
    
    active          = fields.Boolean(string='Aktif', default=True) # active adalah variabel spesial odoo untuk mengarsipkan data atau tidak

    appoinment_id   = fields.Many2one(comodel_name='cdn.appointment', string='Pasien Appointment') # many to one ke tabel cdn appointment
    image           = fields.Image(string='gambar') # field image
    tag_ids         = fields.Many2many(comodel_name='cdn.pasien.tag', string='Tags') # many to many ke tabel cdn pasien tag

    # appoinment_count = fields.Char(compute='_compute_appoinment_count', string='Appoinment Count', store=True)
    appoinment_count = fields.Char(compute='_compute_appoinment_count', string='Appoinment Count')
    appoinment_ids = fields.One2many(comodel_name='cdn.appointment', inverse_name='pasien_id', string='Appoinments')
    
    
    
    parent = fields.Char(string='Parrent')
    is_menikah = fields.Selection(string='Menikah', selection=[('menikah', 'Sudah Menikah'), ('single', 'Single'),])
    parent_name = fields.Char(string='Nama Parner')
     
    
    @api.depends('appoinment_ids')
    def _compute_appoinment_count(self):
        for rec in self:
            rec.appoinment_count = self.env['cdn.appointment'].search_count([('pasien_id', '=', rec.id)])
            # rec.appoinment_count = 10
    
    @api.constrains('tgl_lahir') # fungsi untuk mengecek tanggal lahir pasien tidak boleh lebih dari hari ini
    def _check_tgl_lahir(self):
        for rec in self: # looping untuk mengecek tanggal lahir pasien
            if rec.tgl_lahir > date.today(): # jika tanggal lahir pasien lebih dari hari ini
                raise pesan_error('Tanggal lahir tidak boleh lebih dari hari ini') # tampilkan pesan error
    
    @api.ondelete(at_uninstall=False) # fungsi untuk menghapus data pasien
    def _check_appoinments(self):
        for rec in self: 
            if rec.appoinment_ids: 
                raise pesan_error(_('Tidak bisa menghapus pasien yang memiliki appoinment'))

    @api.model
    def create (self, vals): 
        print("...........", self.env['ir.sequence']) 
        vals['ref'] = self.env['ir.sequence'].next_by_code('nomor.pasien') 
        return super(CdnPasien, self).create(vals) # membuat record baru dengan nilai vals yang di inputkan
    
    def write(self, vals):
        if not self.ref: # jika ref kosong
            vals['ref'] = self.env['ir.sequence'].next_by_code('nomor.pasien') # penomoran
        res = super(CdnPasien, self).write(vals)
        return res 
    
    @api.depends('tgl_lahir') #fungsi untuk menghitung umur pasien berdasarkan tanggal lahir pasien 
    def _compute_umur(self):
        for rec in self: #looping untuk menghitung umur pasien 
            today = date.today() #mengambil tanggal hari ini
            if rec.tgl_lahir: #jika tanggal lahir pasien ada
                rec.umur = today.year - rec.tgl_lahir.year # menghitung umur pasien
            else:
                rec.umur = 0 #jika tidak di kasih else nilai bakal null dan error
    
    
    # https://www.cybrosys.com/blog/how-to-use-of-name-get-function-in-odoo
    # def name_get(self):
    #     result = []
    #     for rec in self:
    #         result.append((rec.id, "{} - {}".format(rec.ref, rec.name)))
    #     return result
    
    def name_get(self): return [(rec.id, "{} {}".format(rec.ref, rec.name)) for rec in self] # fungsi name get untuk menampilkan nama pasien dengan refrensi pasien