import datetime
from odoo import api, fields, models, _
from dateutil import relativedelta
from datetime import date 
from odoo.exceptions import ValidationError as pesan_error

class CdnWzBatalapointment(models.TransientModel):
    _name           = 'cdn.wz.batalapointment'
    _description    = 'Cdn Wz Batalapointment'

    # appointment_id  = fields.Many2one(comodel_name='cdn.pasien', string='Appointment') #keliruu harusnya cdn.appointment
    app_id = fields.Many2one(comodel_name='cdn.appointment', string='Janji Konsultasi', 
                             domain=['|', ('state', '=', 'draf'),('ploritas','in',('0','1', False))])
    # app_id = fields.Many2one(comodel_name='cdn.appointment', string='Janji Konsultasi')
    

    reason          = fields.Text(string='Reason') 
    tanggal_batal   = fields.Date(string='Tanggal Batal')
    
    
    @api.model
    def default_get(self, fields): 
        ref = super (CdnWzBatalapointment, self).default_get(fields)
        ref['tanggal_batal'] = datetime.date.today() 
        ref['reason'] = 'Alasan Batal py'
        # print("............", self.env.context)
        # hasil ............{'lang': 'en_US', 'tz': 'Asia/Jakarta', 'uid': 2, 'allowed_company_ids': [1], 'active_model': 'cdn.appointment', 'active_id': 24, 'active_ids': [24]}
        if self.env.context.get('active_id'): # jika active id ada
            ref['app_id'] = self.env.context.get('active_id') # mengambil active id
        return ref
    

    # fungsi 
    def action_cancel(self): # fungsi cancel untuk mengubah state menjadi cancel
        batal_day = self.env['ir.config_parameter'].get_param('om_hospital.hari_batal') # mengambil nilai dari parameter hari batal
        allowed_date = self.app_id.booking_date - relativedelta.relativedelta(days=int(batal_day))

        print (allowed_date, "<", date.today())
        print (allowed_date < date.today())
        # fungsi ini untuk membatalkan appoinment jika tanggal batal lebih kecil dari hari ini maka tampilkan pesan error
        # contoh kasus di kehidupan nyata jika kita ingin membatalkan appoinment kita harus memberitahu dokter atau rumah sakit
        # minimal 1 hari sebelumnya jika tidak maka akan dikenakan denda
        if allowed_date < date.today(): # jika tanggal batal lebih kecil dari hari ini maka tampilkan pesan error
            raise pesan_error(_("Tidak bisa membatalkan appoinment karena sudah melewati batas hari batal"))

        self.app_id.state = 'cancel' # mengubah state menjadi cancel
        return {
            'type': 'ir.actions.client',
            # 'res_model': 'cdn.appointment',
            # 'view_mode': 'tree',
            'tag' : 'reload',
        }
    