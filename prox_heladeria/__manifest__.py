# -*- coding: utf-8 -*-
{
    'name': "Recetas Heladeria",

    'summary': """Gestión de recetas de helados""",

    'description': """
        Permite tomar nota de las diferentes recetas de helados, clasificar si están listas para producir o en proceso de mejora, su dificultad y calcular algunos aspectos monetarios relacionados con la venta de los mismos
    """,

    'author': "Manuel Gonzalez Poses",
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
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
