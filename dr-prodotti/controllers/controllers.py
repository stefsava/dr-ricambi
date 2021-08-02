# -*- coding: utf-8 -*-
# from odoo import http


# class Dr-prodotti(http.Controller):
#     @http.route('/dr-prodotti/dr-prodotti/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dr-prodotti/dr-prodotti/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dr-prodotti.listing', {
#             'root': '/dr-prodotti/dr-prodotti',
#             'objects': http.request.env['dr-prodotti.dr-prodotti'].search([]),
#         })

#     @http.route('/dr-prodotti/dr-prodotti/objects/<model("dr-prodotti.dr-prodotti"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dr-prodotti.object', {
#             'object': obj
#         })
