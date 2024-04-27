# -*- coding: utf-8 -*-
# from odoo import http


# class OmHospital(http.Controller):
#     @http.route('/om_hospital/om_hospital', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/om_hospital/om_hospital/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('om_hospital.listing', {
#             'root': '/om_hospital/om_hospital',
#             'objects': http.request.env['om_hospital.om_hospital'].search([]),
#         })

#     @http.route('/om_hospital/om_hospital/objects/<model("om_hospital.om_hospital"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('om_hospital.object', {
#             'object': obj
#         })
