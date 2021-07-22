# -*- coding: utf-8 -*-

from odoo import models, fields


class FrancescoCodici(models.Model):

    #_inherit = 'product.template'

    _name = "francesco_codici.codici"
    _description = "description"
    
    #name = fields.Char()
    codice = fields.Char()

# from odoo import models, fields, api


# class test(models.Model):
#     _name = 'test.test'
#     _description = 'test.test'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
