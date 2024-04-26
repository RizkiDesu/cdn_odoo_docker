# -*- coding: utf-8 -*-
# from odoo import http


# class CdnTraining(http.Controller):
#     @http.route('/cdn_training/cdn_training', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cdn_training/cdn_training/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cdn_training.listing', {
#             'root': '/cdn_training/cdn_training',
#             'objects': http.request.env['cdn_training.cdn_training'].search([]),
#         })

#     @http.route('/cdn_training/cdn_training/objects/<model("cdn_training.cdn_training"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cdn_training.object', {
#             'object': obj
#         })
