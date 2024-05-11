from odoo import api, fields, models
from odoo.tools.safe_eval import safe_eval

class OdooPlaygroud(models.Model):
    _name = 'odoo.playgroud'
    _description = 'Odoo Playgroud'

    DEFAULT_ENV_VARIABLES = """ # sumary_line
    # input your code here
    # in line 
    # for example
    # print('Hello World')

    """
    
    model_id = fields.Many2one(comodel_name='ir.model', string='Model')
    code = fields.Text(string='Code', default=DEFAULT_ENV_VARIABLES)
    result = fields.Text(string='Result')

    def action_execute(self):
        try:
            if self.model_id:
                model = self.env[self.model_id.model]
            else:
                model = self
            self.result = safe_eval(self.code, {'self': self, 'model': model})
        except Exception as e:
            self.result = str(e)