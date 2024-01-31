# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details
from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm_sale(self):
        for sale_order_id in self:
            sale_order_id.action_confirm()

    def action_cancel_sale(self):
        active_ids = self._context.get('active_ids')
        sale_order_ids = self.env['sale.order'].browse(active_ids)
        for sale_order_id in sale_order_ids:
            if sale_order_id.state == 'draft' or sale_order_id.state == 'sent' or sale_order_id.state == 'sale':
                sale_order_id.action_cancel()

            for sale_picking_id in sale_order_id.picking_ids:
                if not sale_order_id.state == 'cancel' and sale_picking_id.state == 'done' or sale_order_id.invoice_ids.state == 'draft':
                    user_error_wizard_id = self.env['sale.order.cancel.wizard'].create({
                        'message': f"Some products of Sale Order {[i.origin for i in sale_order_ids.picking_ids if i.state == 'done']} already been delivered. Returns can be created from the Delivery Orders."

                    })
                    return {
                        'name': _('Cancel Sales Order'),
                        'type': 'ir.actions.act_window',
                        'view_mode': 'form',
                        'res_model': 'sale.order.cancel.wizard',
                        'res_id': user_error_wizard_id.id,
                        'target': 'new',
                        'context': self.env.context
                    }
