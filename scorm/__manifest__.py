# -*- coding: utf-8 -*-
{
    'name': "SCORM",

    'summary': """
        This module add the ability of importing scorm package into Odoo e-Learning""",
    'author': "Business Solution Advisors",
    'website': "http://www.bsa-me.com",
    'category': 'Website',
    'version': '0.1',
    'application': True,
    # any module necessary for this one to work correctly
    'depends': ['base', 'website_slides'],
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
