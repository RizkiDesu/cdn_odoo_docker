# -*- coding: utf-8 -*-
# from odoo import http


# class OmHospitalInherit(http.Controller):
#     @http.route('/om_hospital_inherit/om_hospital_inherit', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/om_hospital_inherit/om_hospital_inherit/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('om_hospital_inherit.listing', {
#             'root': '/om_hospital_inherit/om_hospital_inherit',
#             'objects': http.request.env['om_hospital_inherit.om_hospital_inherit'].search([]),
#         })

#     @http.route('/om_hospital_inherit/om_hospital_inherit/objects/<model("om_hospital_inherit.om_hospital_inherit"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('om_hospital_inherit.object', {
#             'object': obj
#         })
