# -*- coding: utf-8 -*-
# from odoo import http


# class VendorExtension(http.Controller):
#     @http.route('/vendor_extension/vendor_extension', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vendor_extension/vendor_extension/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vendor_extension.listing', {
#             'root': '/vendor_extension/vendor_extension',
#             'objects': http.request.env['vendor_extension.vendor_extension'].search([]),
#         })

#     @http.route('/vendor_extension/vendor_extension/objects/<model("vendor_extension.vendor_extension"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vendor_extension.object', {
#             'object': obj
#         })
