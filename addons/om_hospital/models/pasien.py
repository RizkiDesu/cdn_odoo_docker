from odoo import api, fields, models,_
from datetime import date
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError as pesan_error

class CdnPasien(models.Model):
    _name           = 'cdn.pasien' # nama tabel di database
    _description    = 'Cdn Pasien' # deskripsi tabel di database
    _inherit        = ['mail.thread','mail.activity.mixin'] # tambahkan mail thread untuk mengirim email
    

    name            = fields.Char(string='Nama Pasien', tracking=True) # field nama pasien
    tgl_lahir       = fields.Date(string='Tangggal Lahir') # field tanggal lahir
    # ref             = fields.Char(string='Refrensi', default='Odoo Mates') # field refrensi dengan nilai default Odoo Mates
    ref             = fields.Char(string='Refrensi') # field refrensi 

    umur            = fields.Integer(string='Umur', tracking=True, 
                                     compute='_compute_umur', search='_search_umur',
                                     inverse='_inverse_compute_umur' )  
    # field umur dengan fungsi compute _compute_umur untuk menghitung umur pasien berdasarkan tanggal lahir pasien
    
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
    appoinment_count = fields.Integer(compute='_compute_appoinment_count', string='Appoinment Count', store=True)
    appoinment_ids = fields.One2many(comodel_name='cdn.appointment', inverse_name='pasien_id', string='Appoinments')
    
    # is_ulangtahun = fields.Boolean(string='Ulang tahun', compute='_compute_is_ulangtahun')
    
    
    parent = fields.Char(string='Parrent')
    is_menikah = fields.Selection(string='Menikah', selection=[('menikah', 'Sudah Menikah'), ('single', 'Single'),])
    parent_name = fields.Char(string='Nama Parner')
    
    phone = fields.Char(string='Nomor Telepon')
    email = fields.Char(string='Email')
    website = fields.Char(string='Website')
    

    
    @api.depends('appoinment_ids')
    def _compute_appoinment_count(self):
        for rec in self:
            rec.appoinment_count = self.env['cdn.appointment'].search_count([('pasien_id', '=', rec.id)])
            # rec.appoinment_count = 10
    
    @api.constrains('tgl_lahir') # fungsi untuk mengecek tanggal lahir pasien tidak boleh lebih dari hari ini
    def _check_tgl_lahir(self):
        for rec in self: # looping untuk mengecek tanggal lahir pasien
            if rec.tgl_lahir and rec.tgl_lahir :
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
    @api.depends('umur')
    def _inverse_compute_umur(self):
        for rec in self:
            today = date.today()
            rec.tgl_lahir = today - relativedelta(years=rec.umur)
    
    def _search_umur(self, operator, value): # fungsi untuk mencari umur pasien
        tgl_lahir = date.today() - relativedelta(years=value)
        start_of_year = tgl_lahir.replace(day=1, month=1)
        end_of_year = tgl_lahir.replace(day=31, month=12)
        return [('tgl_lahir', '>=', start_of_year), ('tgl_lahir', '<=', end_of_year)]
        
    # https://www.cybrosys.com/blog/how-to-use-of-name-get-function-in-odoo
    # def name_get(self):
    #     result = []
    #     for rec in self:
    #         result.append((rec.id, "{} - {}".format(rec.ref, rec.name)))
    #     return result
    
    def name_get(self): return [(rec.id, "[{}] {}".format(rec.ref, rec.name)) for rec in self] # fungsi name get untuk menampilkan nama pasien dengan refrensi pasien

    def action_test (self): 
        print('test')
        return True
    
    is_ulangtahun = fields.Boolean(string='Ulang tahun', compute='_compute_is_ulangtahun')
    @api.depends('tgl_lahir') # override berfungsi untuk mengutamakan `tgl_lahir` pada `@api.depends
    def _compute_is_ulangtahun(self):
        is_ulangtahun = False
        for rec in self:
            hari_ini = date.today()
            print("-----------------")
            print("tgl ini", hari_ini.day, "== tgl lahir", rec.tgl_lahir.day,
                  "dan bulan lahir", rec.tgl_lahir.month, "== bulan ini", hari_ini.month,)
            print("hasil logika :",rec.tgl_lahir.month == hari_ini.month 
                  and rec.tgl_lahir.day == hari_ini.day)
            if rec.tgl_lahir: # jika tanggal lahir pasien ada
                # jika bulan lahir = bulan hari ini dan tanggal lahir = tanggal hari ini maka is_ulangtahun = True
                if rec.tgl_lahir.month == hari_ini.month and rec.tgl_lahir.day == hari_ini.day:
                    is_ulangtahun = True
                else:
                    is_ulangtahun = False
            rec.is_ulangtahun = is_ulangtahun
    