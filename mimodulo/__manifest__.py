# -*- coding: utf-8 -*-
{
    'name': "mimodulo",

    'summary': """
              This modules provides functionalities to manage ice cream recipes in the context of an ice cream shop
""",

    'description': """
    This module is intended for the world of cuisine, namely, for ice cream shops. Its aim is to allow the user to manage all their own recipes, establishing -among other things- the creator of the recipe, modify those recipes that were previously created, their state of developement and, of course, the recipe itself with its steps.
    """,

    'author': "Manuel Gonzalez",
    'website': "https://github.com/conversorbinario",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/helados.xml',
        'views/reposteros.xml',
        'views/sorbetes.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}