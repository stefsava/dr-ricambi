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

    name = fields.Char()

    def get_json(self):
        url = "https://francescodattolo.it/tmp/test.json"
        response = requests.get(url)
        json_data = response.json()
        loaded_json = json.dumps(json_data)

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
