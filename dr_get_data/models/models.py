# -*- coding: utf-8 -*-
import requests
import json

from odoo import models, fields, api

from odoo.exceptions import UserError
from odoo.tools.translate import _

# LOGGING
import logging
_logger = logging.getLogger(__name__)

class dr_get_data(models.Model):
    _name = 'dr_get_data.dr_get_data'

    name = fields.Char(required=True)

    @api.model
    def get_json(self,vals):
        url = "https://francescodattolo.it/tmp/test.json"
        response = requests.get(url)
        json_data = response.json()
        loaded_json = json.dumps(json_data)

        _logger.info("############################## self: "+str(self))

        _logger.info("############################## vals: "+str(vals))

        for o in self:
            _logger.info("############################## obj in self: "+str(o))

        member = self.env['dummy.json.members'].create(
            {
            'name': 'Pippo Franco',
            'age': '47',
            'secret_identity': 'Rabbit'
            }
        )

        _logger.info("############################## member: "+str(member))


        raise UserError(str(loaded_json))

# class dr-prodotti(models.Model):
#     _name = 'dr-prodotti.dr-prodotti'
#     _description = 'dr-prodotti.dr-prodotti'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
