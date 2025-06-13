# -*- coding: utf-8 -*-
#################################################################################
# Author      : Terabits Technolab (<www.terabits.xyz>)
# Copyright(c): 2021
# All Rights Reserved.
#
# This module is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#################################################################################
{
    'name': 'Advanced Web Domain Widget',
    'version': '15.0.3.0.1',
    'summary': 'Set all relational fields domain by selecting its records unsing `in, not in` operator.',
    'sequence': 10,
    'author': 'Terabits Technolab',
    'license': 'OPL-1',
    'website': 'https://www.terabits.xyz',
    'description':"""
      
        """,
    "price": "29.00",
    "currency": "USD",
    'depends':['base','web'],
    'data':[
        # 'views/assets.xml',
    ],
    'assets': {
        'web.assets_qweb': [
            "/advanced_web_domain_widget/static/src/xml/domain_base.xml",
        ],
        'web.assets_backend': [
            "/advanced_web_domain_widget/static/src/js/fields/basic_fields.js",
            "/advanced_web_domain_widget/static/src/js/fields/terabits_fields_registry.js",
            "/advanced_web_domain_widget/static/src/scss/style.scss",
            "/advanced_web_domain_widget/static/src/js/widget/domain_selector_dialog.js",
            "/advanced_web_domain_widget/static/src/js/widget/model_field_selector.js",
            "/advanced_web_domain_widget/static/src/js/widget/model_record_selector.js",
            "/advanced_web_domain_widget/static/src/js/widget/TerabitsDomainSelector.js",
            
        ],
        
    },
    'images': ['static/description/banner.png'],
    'application': True,
    'installable': True,
    'auto_install': False,
}
