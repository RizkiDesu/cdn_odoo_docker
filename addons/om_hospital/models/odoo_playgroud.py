from odoo import api, fields, models
from odoo.tools.safe_eval import safe_eval # digunakan untuk menjalankan code python nanti

class OdooPlaygroud(models.Model):
    _name = 'odoo.playgroud'
    _description = 'Odoo Playgroud'

    DEFAULT_DATA_CODE = """ 
    # sumary_line
    # input your code here
    # in line 
    # for example
    # print('Hello World')
    """
    
    model_id = fields.Many2one(comodel_name='ir.model', string='Model')
    code = fields.Text(string='Code', default = DEFAULT_DATA_CODE)
    result = fields.Text(string='Result')

    def action_execute(self):
        try: # mencoba menjalankan code
            if self.model_id: # jika model id ada
                model = self.env[self.model_id.model] 
            else:
                model = self #
            self.result = safe_eval(self.code, {'self': self, 'model': model}) # menjalankan code
        except Exception as e: # jika terjadi error
            self.result = str(e) # pesan error jika terjadi error