# -*- encoding: utf-8 -*-

{
    'name': 'Jordan Chart of Accounts standard',
    'version': '15.0.0.0',
    'author': "mohamed kiwan",
    'website': "",
    'category': 'Localization',
    'sequence': -100,
    'description': """
     Jordan localization.
    """,
    'depends': ['account'],
    'data': [
        'data/account_chart_template_data.xml',
        # 'data/account.group.csv',
        # 'data/account.account.template.csv',
        'data/account_tax_group_data.xml',
        'data/account_tax_template_data.xml',
        'data/l10n_jo_chart_data.xml',
        'data/account_chart_template_conf_data.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'post_init_hook': 'load_translations',
}
