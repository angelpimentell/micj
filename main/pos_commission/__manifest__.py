# -*- coding: utf-8 -*-
{
    'name': "pos_commission",

    'summary': """
        Calculator to streamline the process of calculating 
        commissions for sales representatives based 
        on Point of Sale (POS) transactions.""",

    'description': """
        Calculator to streamline the process of calculating 
        commissions for sales representatives based 
        on Point of Sale (POS) transactions.
    """,

    'author': "Angel Pimentel",
    'website': "https://do.linkedin.com/in/angel-pimentell/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale', 'contacts', 'report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',

        'views/product_template/product_template_form.xml'
        'views/pos_commission_wizard/pos_commission_wizard_form.xml',
        'views/pos_commission_wizard/pos_commission_wizard_menuitem.xml',
    ],
}
