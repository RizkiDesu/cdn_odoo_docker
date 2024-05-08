# -*- coding: utf-8 -*-
# from odoo import http


# class OmHospitalTest(http.Controller):
#     @http.route('/om_hospital_test/om_hospital_test', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/om_hospital_test/om_hospital_test/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('om_hospital_test.listing', {
#             'root': '/om_hospital_test/om_hospital_test',
#             'objects': http.request.env['om_hospital_test.om_hospital_test'].search([]),
#         })

#     @http.route('/om_hospital_test/om_hospital_test/objects/<model("om_hospital_test.om_hospital_test"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('om_hospital_test.object', {
#             'object': obj
#         })
