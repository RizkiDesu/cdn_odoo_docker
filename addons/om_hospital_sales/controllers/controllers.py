# -*- coding: utf-8 -*-
# from odoo import http


# class OmHospitalSales(http.Controller):
#     @http.route('/om_hospital_sales/om_hospital_sales', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/om_hospital_sales/om_hospital_sales/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('om_hospital_sales.listing', {
#             'root': '/om_hospital_sales/om_hospital_sales',
#             'objects': http.request.env['om_hospital_sales.om_hospital_sales'].search([]),
#         })

#     @http.route('/om_hospital_sales/om_hospital_sales/objects/<model("om_hospital_sales.om_hospital_sales"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('om_hospital_sales.object', {
#             'object': obj
#         })
