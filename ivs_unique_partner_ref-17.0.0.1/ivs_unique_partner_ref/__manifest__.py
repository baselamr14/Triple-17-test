# -*- coding: utf-8 -*-
{
    'name': """Unique Partner Reference""",
    'summary': """Set the Reference (Code) on Partners to be Unique per partner""",
    'description': """Installing this module will make the field (Reference) on the Partner form unique, so you can add the partners code without duplication""",
    'author': 'I Value Solutions',
    'website': 'https://www.ivalue-s.com',
    'email': 'info@ivalue-s.com',
    'license':'OPL-1',	
    'category': 'Accounting',
    'version': '17.0.0.1',
    'images': ['static/description/banner.png'],
    'depends': ['base', 'web', 'contacts'],

    'data': [
        # 'security/ir.model.access.csv',
        # 'security/security.xml',
        'views/res_partner.xml',
    ],
    
    
}
