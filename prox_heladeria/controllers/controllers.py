# -*- coding: utf-8 -*-
from odoo import http

# class ProxHeladeria(http.Controller):
#     @http.route('/prox_heladeria/prox_heladeria/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/prox_heladeria/prox_heladeria/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('prox_heladeria.listing', {
#             'root': '/prox_heladeria/prox_heladeria',
#             'objects': http.request.env['prox_heladeria.prox_heladeria'].search([]),
#         })

#     @http.route('/prox_heladeria/prox_heladeria/objects/<model("prox_heladeria.prox_heladeria"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('prox_heladeria.object', {
#             'object': obj
#         })