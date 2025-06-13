from odoo import fields, models, api, _
from odoo.exceptions import UserError


class res_users(models.Model):
    _inherit = 'res.users'

    access_management_ids = fields.Many2many('access.management', 'access_management_users_rel_ah', 'user_id', 'access_management_id', 'Access Pack')

    # allow_ip_ids = fields.One2many('allow.ip', 'user_id', 'Allow IP')
    
    def write(self, vals):
        res = super(res_users, self).write(vals)
        for access in self.access_management_ids:
            if self.env.company in access.company_ids and access.readonly:
                if self.has_group('base.group_system') or self.has_group('base.group_erp_manager'):
                    raise UserError(_('Admin user can not be set as a read-only..!'))
        return res

    @api.model
    def create(self, vals):
        res = super(res_users, self).create(vals)
        for access in res.access_management_ids:    
            if self.env.company in access.company_ids and access.readonly:
                if res.has_group('base.group_system') or res.has_group('base.group_erp_manager'):
                    raise UserError(_('Admin user can not be set as a read-only..!'))
        return res
