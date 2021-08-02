# Copyright (C) 2018 - TODAY, Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Customization of the 'Unique Product Internal Reference' OCA module",
    "summary": "Set Product Internal Reference and Product brand  with as Unique",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "author": "Open Source Integrators, Odoo Community Association (OCA)",
    "category": "Product",
    "website": "https://github.com/OCA/product-attribute",
    "depends": ["product"],
    "pre_init_hook": "pre_init_product_code",
    "installable": True,
}