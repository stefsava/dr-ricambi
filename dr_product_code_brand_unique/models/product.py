# Copyright (C) 2018 - TODAY, Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class ProductProduct(models.Model):
    _inherit = "product.template"

    _sql_constraints = [
        (
            "default_code_uniq",
            "unique(default_code, product_brand_id)",
            "Internal Reference and brand must be unique across the database!",
        )
    ]
