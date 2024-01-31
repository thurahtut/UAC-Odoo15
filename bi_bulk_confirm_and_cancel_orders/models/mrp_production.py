# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details
from odoo import api, fields, models, _
from odoo.exceptions import UserError


class MrpProduction(models.Model):
    _inherit = "mrp.production"

    def action_confirm_mo(self):
        for rec in self:
            rec.action_confirm()
        for rec in self:
            if rec.state == 'cancel' or rec.state == 'done' or rec.state == 'progress':
                raise UserError("It is not allowed to confirm an order in the following states : progress, done, cancel")


    def action_cancel_mo(self):
        active_ids = self._context.get('active_ids')
        mrp_production_ids = self.env['mrp.production'].browse(active_ids)
        for mrp_production_id in mrp_production_ids:
            if mrp_production_id.state == 'draft' or mrp_production_id.state == 'confirmed' or mrp_production_id.state == 'progress':
                mrp_production_id.action_cancel()
            if mrp_production_id.state == 'done':
                raise UserError("Cannot cancel a manufacturing order in done state.")

