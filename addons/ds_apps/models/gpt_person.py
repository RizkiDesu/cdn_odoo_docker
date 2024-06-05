from odoo import models, fields

class Person(models.Model):
    _name = 'crud.person'
    _description = 'Person'

    name = fields.Char(string='Name')
    email = fields.Char(string='Email')
    age = fields.Integer(string='Age')
    image = fields.Binary(string='Image')
