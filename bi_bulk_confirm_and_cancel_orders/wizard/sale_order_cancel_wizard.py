# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, _


class SaleOrderCancelWizard(models.TransientModel):
    _name = "sale.order.cancel.wizard"
    _description = "Sale Order Cancel Wizard"

    message = fields.Text('message', readonly=True)

    def button_confirm_sale_order(self):
        active_id = self._context.get('active_ids')
        sale_order_ids = self.env['sale.order'].browse(active_id)

        for sale_order_id in sale_order_ids:
            if sale_order_id.state == 'draft' or sale_order_id.state == 'sent' or sale_order_id.state == 'sale':
                sale_order_id._action_cancel()
            for sale_order_id in sale_order_ids:
                for sale_picking_id in sale_order_id.picking_ids:
                    if not sale_picking_id.state == 'done':
                        sale_picking_id.action_cancel()
