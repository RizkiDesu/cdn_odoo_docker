# -*- coding: utf-8 -*-
{
    'name': "Om Hospital",

    'summary': """
        Dibuat dalam rangka pelatihan odoo denga refrensi pada youtube""",

    'description': """
      halaman deskripsi pajang
    """,

    'author': "rizki desu",
    'website': "rizkidesu.github.io",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Hospital',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'aplication':True,
}
