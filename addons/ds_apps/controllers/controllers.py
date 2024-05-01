# -*- coding: utf-8 -*-
# from odoo import http


# class DsApps(http.Controller):
#     @http.route('/ds_apps/ds_apps', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ds_apps/ds_apps/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ds_apps.listing', {
#             'root': '/ds_apps/ds_apps',
#             'objects': http.request.env['ds_apps.ds_apps'].search([]),
#         })

#     @http.route('/ds_apps/ds_apps/objects/<model("ds_apps.ds_apps"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ds_apps.object', {
#             'object': obj
#         })
