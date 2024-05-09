# -*- coding: utf-8 -*-
# from odoo import http


# class OmSales(http.Controller):
#     @http.route('/om_sales/om_sales', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/om_sales/om_sales/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('om_sales.listing', {
#             'root': '/om_sales/om_sales',
#             'objects': http.request.env['om_sales.om_sales'].search([]),
#         })

#     @http.route('/om_sales/om_sales/objects/<model("om_sales.om_sales"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('om_sales.object', {
#             'object': obj
#         })
