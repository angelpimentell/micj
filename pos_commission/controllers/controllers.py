# -*- coding: utf-8 -*-
# from odoo import http


# class PosCommission(http.Controller):
#     @http.route('/pos_commission/pos_commission/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_commission/pos_commission/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_commission.listing', {
#             'root': '/pos_commission/pos_commission',
#             'objects': http.request.env['pos_commission.pos_commission'].search([]),
#         })

#     @http.route('/pos_commission/pos_commission/objects/<model("pos_commission.pos_commission"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_commission.object', {
#             'object': obj
#         })
