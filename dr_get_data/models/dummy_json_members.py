# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo.exceptions import UserError
from odoo.tools.translate import _

# LOGGING
import logging
_logger = logging.getLogger(__name__)

class DummyJsonMembers(models.Model):
    _name = 'dummy.json.members'

    name = fields.Char()
    age = fields.Char()
    secret_identity = fields.Char()