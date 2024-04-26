from odoo import models, fields, api

class TrainingCourse(models.Model):
    _name               = 'training.course'
    _description        = 'Training Course'

    name                = fields.Char(string='Nama Kursus', required=True)
    description         = fields.Text(string='Keterangan')
    user_id             = fields.Many2one(comodel_name='res.users', string='Penanggung Jawab')

    session_line        = fields.One2many(comodel_name='training.session', inverse_name='course_id', string='Sesi Training')

    # oofco 
    _sql_constraints    = [
        ("name_course_unique", "UNIQUE(name)", "Nama Kursus Sudah Ada"),
    ]
    
class TrainingSession(models.Model):
    _name               = 'training.session'
    _description        = 'Training Session'

    name                = fields.Char(string='Sesi Trainig', required=True)
    course_id           = fields.Many2one(comodel_name='training.course', string='Nama Kursus', required=True)
    start_date          = fields.Date(string='Tanggal Mulai', required=True)
    duration            = fields.Float(string='Durasi (s)', required=True)
    seats               = fields.Integer(string='MAX Peserta', required=True, default=1)
    instruktur_id       = fields.Many2one(comodel_name='instruktur', string='Nama Instruktur')
    
    alamat              = fields.Char(string='Alamat', related='instruktur_id.street')
    no_hp               = fields.Char(string='No Hp', related='instruktur_id.mobile')
    email               = fields.Char(string='Email', related='instruktur_id.email')
    jenis_kel           = fields.Selection(string='Jenis Kelamin', related='instruktur_id.jenis_kel')