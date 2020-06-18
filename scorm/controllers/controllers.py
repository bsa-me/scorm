# -*- coding: utf-8 -*-
# from odoo import http


# class Scorm(http.Controller):
#     @http.route('/scorm/scorm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/scorm/scorm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('scorm.listing', {
#             'root': '/scorm/scorm',
#             'objects': http.request.env['scorm.scorm'].search([]),
#         })

#     @http.route('/scorm/scorm/objects/<model("scorm.scorm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('scorm.object', {
#             'object': obj
#         })
