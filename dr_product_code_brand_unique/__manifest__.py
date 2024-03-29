# Copyright (C) 2018 - TODAY, Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "DR Unique Product Internal Reference and Brand",
    "summary": "Set Product Internal Reference ad Brand as Unique",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "author": "Open Source Integrators, Odoo Community Association (OCA)",
    "category": "drricambi",
    "website": "https://github.com/OCA/product-attribute",
    "depends": [
        "product",
        "product_brand",
        ],
    "pre_init_hook": "pre_init_product_code",
    "installable": True,
    "auto_install": True,

}
