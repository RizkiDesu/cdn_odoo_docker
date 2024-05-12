from odoo import api, fields, models
from odoo.tools.safe_eval import safe_eval 

class OdooPlaygroud(models.Model):
    _name = 'odoo.playgroud'
    _description = 'Odoo Playgroud'

    DEFAULT_DATA_CODE = """ 
    # Example code
    # self is the current record
    # self.env is the environment
    # self.env.user is the current user
    # self.env['model.name'] is the model
    # self.env['model.name'].search([]) to search records
    # self.env.is_superuser() to check if the user is a superuser
    # self.env.user.company_id to get the company of the user
    # self.env.is_admin() to check if the user is an admin
    # self.env.user.company_id to get the company of the user
    # self.env.context to get the context
    # self.env.cr to get the cursor
    """
    
    model_id = fields.Many2one(comodel_name='ir.model', string='Model')
    code = fields.Text(string='Code', default = DEFAULT_DATA_CODE)
    result = fields.Text(string='Result')

    def action_execute(self):
        try: 
            if self.model_id: 
                model = self.env[self.model_id.model] 
            else:
                model = self 
            self.result = safe_eval(self.code.strip(), {'self': model})
        except Exception as e: 
            self.result = str(e) 