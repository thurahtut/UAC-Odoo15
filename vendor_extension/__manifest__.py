# -*- coding: utf-8 -*-
{
    'name': "Vendor Extension",

    'summary': """
        This module is intended to add more fields and functions into res.partner(Vendor) model.""",

    'description': """
        This module is intended to add more fields and functions into res.partner(Vendor) model.
    """,

    'author': "Super Seven Stars",
    'website': "",
    'license': "AGPL-3",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/vendor_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
