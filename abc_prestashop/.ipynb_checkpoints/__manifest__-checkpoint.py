# -*- coding: utf-8 -*-
{
    'name': "abc_prestashop",

    'summary': """
        Modulo che contiene le funzioni per l'interscambio dati verso Prestashop.""",

    'description': """
        Modulo che contiene le funzioni per l'interscambio dati verso Prestashop.
    """,

    'author': "A.B.C. srl",
    'website': "https://www.abcstrategie.it/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'API',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'sale_management', 'pos_sale', 'sale_enterprise', 'sale_margin', 'sale_stock', 'point_of_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
    ],
     "installable": True,

}
