# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
{
    "name": "Bulk Confirm Orders | Bulk Cancel Orders",
    "version": "15.0.0.2",
    "category": "Extra Tools",
    "summary": "Confirm Orders in Bulk Confirm Sales Orders Cancel Orders in Bulk Cancel Purchase Order Mass Order Confirm in Manufacturing Orders Mass Order Cancel Sale Order Bulk Order Cancel in Purchase Bulk Confirm Orders in MRP Order Mass Confirm Orders Manufacturing",
    "description": """

        Bulk Confirm  and Cancel Orders Odoo App helps users to cancel and confirm orders in bulk for sales order, purchase order and manufacturing order. User have to just select order in bulk then select the confirm or cancel option based on that it will confirmed or cancelled as per selected option and the order will be moved as per that stage.

    """,
    "author": "BrowseInfo",
    "website": "https://www.browseinfo.com",
    "depends": ["base",
                "crm",
                "sale",
                "sale_management",
                "purchase",
                "mrp"
                ],
    "data": [
            "security/ir.model.access.csv",
            "wizard/sale_order_cancel_wizard_view.xml",
            "views/sale_order_view.xml",
            "views/purchase_order_view.xml",
            "views/mrp_production_view.xml",

        ],
    'license':'OPL-1',
    'installable': True,
    'auto_install': False,
    'live_test_url':'https://youtu.be/Hui2AGoPt-c',
    "images":['static/description/Bulk-Confirm-Orders-Banner.gif'],
}

