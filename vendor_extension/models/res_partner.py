# -*- coding: utf-8 -*-
from odoo import _, api, fields, models, tools

class ResPartnerVendorInherit(models.Model):
    _inherit = 'res.partner'

    supplier_type = fields.Selection([('trade_supplier', 'Trade Supplier'),('non_trade_supplier', 'Non Trade Supplier')], string='Supplier Type')
    
    # @api.model
    # def create(self, values):
    #     result = super().create(values)
        
    #     return result
