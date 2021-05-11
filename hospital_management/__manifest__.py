# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Hospital Management',
    'version': '1.0',
    'category': 'Productivity',
    'description': "Hospital management",
    'summary': '',
    'sequence': 260,
    'depends': ['base', 'contacts', 'hr'],
    'data': ['security/ir.model.access.csv',
             'views/patient.xml', 'views/op.xml', 'data/sequence.xml', 'views/contactdob.xml', 'views/consultation.xml', 'views/appoinment.xml', 'views/desease.xml',],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
