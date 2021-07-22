# -*- coding: utf-8 -*-
{
    'name': "francesco_codici",

    'summary': "Francesco Dattolo Codici"
    
    """
        Pure Test Step 
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Pure Test Step Long description of module's purpose
    """,

    'author': "Francesco Dattolo",
    'website': "https://francescodattolo.it",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'drricambi',
    'version': '0.0.3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product'],

    # always loaded
    'data': [
        #'data/francesco_codici_data.xml',
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
  		'views/menu_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
