# -*- coding: utf-8 -*-
{
    'name': 'Hospital',
    'version': '1.0.0',
    'summary': 'Odoo 16 Development Tutorials',
    'sequence': -1000,
    'description': """Odoo 16 Development Tutorials""",
    'category': 'Hospital',
    'author': 'rizki',
    'maintainer': 'Odoo Mates',
    'website': 'https://www.odoomates.tech',
    'license': 'AGPL-3',
    'depends': ['base','mail','product'], # menambahakan dependensi 
    'data': [
        # 'security/groups.xml',
        'security/ir.model.access.csv', #menambahkan security ir.model.access.csv 
        'data/pasien_tag_data.xml', 
        'data/cdn.pasien.tag.csv', #nama ikut model
        'data/sequence_data.xml',
        'wizards/cancel_appointment.xml',
        'views/menu.xml',
        # 'views/dokter_list.xml',
        'views/pasien.xml',
        'views/pasien_perempuan.xml',
        # 'views/test.xml',
        'views/appointment.xml',
        'views/pasien_tag.xml', 
    ], 
    'aplication':True, #menambahkan aplication

}
