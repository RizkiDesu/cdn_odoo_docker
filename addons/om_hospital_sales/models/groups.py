
from odoo import api, fields, models,_


# untuk menghapus setting
class ResGroups(models.Model):
    _inherit = 'res.groups'
    # @api.model
    def get_application_groups(self, domain):
        print("domain:",domain)
        group_id = self.env.ref('project.group_project_task_dependencies').id
        wave_group_id = self.env.ref('stock.group_stock_picking_wave').id
        # return super(ResGroups, self).get_application_groups(domain + [('id', '!=', group_id)])
        return super(ResGroups, self).get_application_groups(domain + [('id', 'not in', (group_id, wave_group_id ))])


