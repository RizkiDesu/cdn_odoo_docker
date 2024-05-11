from odoo import api, fields, models
from datetime import date

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

    appoinment_id   = fields.Many2one(comodel_name='cdn.appointment', string='Pasien') # many to one ke tabel cdn appointment
    image           = fields.Image(string='gambar') # field image
    tag_ids         = fields.Many2many(comodel_name='cdn.pasien.tag', string='Tags') # many to many ke tabel cdn pasien tag

    @api.model
    def create (self, vals): # fungsi create untuk membuat record baru

        print("...........", self.env['ir.sequence']) # print untuk mengecek apakah ir.sequence sudah terbaca atau belum

        # contoh isi adalah vals = {'__last_update': False, 'image': False, 'name': 'nama pasien', 'tgl_lahir': '2024-05-07', 'appoinment_id': 14, 'ref': 'Odoo Mates', 'jenis_kel': 'l', 'tag_ids': [[6, False, [18]]], 'active': True}
        
        vals['ref'] = self.env['ir.sequence'].next_by_code('cdn.pasien') # mengisi ref dengan sequence ir.sequence dengan code cdn.pasien
        
        # vals['ref'] = vals['ref'] or 'Odoo Mates' # jika ref tidak di isi maka ref akan di isi dengan Odoo Mates
        # vals['ref'] = 'Odoo Mates' # mengisi ref dengan Odoo Mates

        return super(CdnPasien, self).create(vals) # membuat record baru dengan nilai vals yang di inputkan
    
    def write(self, vals): # fungsi write untuk mengubah record yang sudah ada
        # print("write methot trigerr", vals) # print untuk mengecek apakah vals sudah terbaca atau belum
        # # output : write methot trigerr {'tgl_lahir': '2000-03-10'}
        # res = super(CdnPasien, self).write(vals) 
        # return res
        if not self.ref: # jika ref kosong
            vals['ref'] = self.env['ir.sequence'].next_by_code('cdn.pasien') # mengisi ref dengan sequence ir.sequence dengan code cdn.pasien
        res = super(CdnPasien, self).write(vals) # mengubah record yang sudah ada
        # hasil jika di database ada nilainya maka gak brubah jika tidak ada maka akan di isi dengan sequence ir.sequence dengan code cdn.pasien
        return res 
    
    @api.depends('tgl_lahir') #fungsi untuk menghitung umur pasien berdasarkan tanggal lahir pasien 
    def _compute_umur(self):
        for rec in self: #looping untuk menghitung umur pasien 
            today = date.today() #mengambil tanggal hari ini
            if rec.tgl_lahir: #jika tanggal lahir pasien ada
                rec.umur = today.year - rec.tgl_lahir.year # menghitung umur pasien
            else:
                rec.umur = 0 #jika tidak di kasih else nilai bakal null dan error

    # def name_get(self):
    #     result = []
    #     for rec in self:
    #         result.append((rec.id, "{} - {}".format(rec.ref, rec.name)))
    #     return result
    
    def name_get(self): return [(rec.id, "{} {}".format(rec.ref, rec.name)) for rec in self]