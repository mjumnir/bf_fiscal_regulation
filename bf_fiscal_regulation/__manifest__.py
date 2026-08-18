# -*- coding: utf-8 -*-
{
    'name': "Burkina Faso - Fiscal Regulation (IFU / RCCM)",
    'summary': "Adds IFU, RCCM, tax regime and fiscal division to partners, "
               "companies, and sale/invoice documents to comply with "
               "Burkina Faso (DGI) fiscal requirements.",
    'description': """
Burkina Faso Fiscal Regulation
===============================
This module adds the fiscal identification fields required by the
Direction Générale des Impôts (DGI) of Burkina Faso:

* N° IFU (Identifiant Financier Unique)
* N° RCCM (Registre du Commerce et du Crédit Mobilier)
* Régime d'imposition (tax regime)
* Division fiscale (fiscal division)

These fields are added to:

* Contacts (res.partner) - required for companies, optional for
  individual contacts.
* Companies (res.company) - always required.
* The Sale Order report and the Customer Invoice report, which now
  display the company's fiscal identity and, when available, the
  customer's IFU / RCCM.

Two new configuration lists are provided so IFU/RCCM regimes and
fiscal divisions can be maintained without touching the code:

* Régime d'imposition (bf.regime.impot)
* Division fiscale (bf.division.fiscale)
""",
    'version': '17.0.1.0.0',
    'category': 'Accounting/Localizations',
    'author': 'Mjumnir (Unik Uslug)',
    'website': 'https://github.com/mjumnir/bf_fiscal_regulation/tree/17.0/bf_fiscal_regulation',
    'maintainers': ['mjumnir'],
    'support': 'mjumnir@gmail.com',
    'license': 'LGPL-3',
    'icon': '/bf_fiscal_regulation/static/description/icon.png',
    "images": ["static/description/banner.png"],
    'countries': ['bf'],
    'depends': ['base', 'contacts', 'sale', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/bf_regime_impot_views.xml',
        'views/bf_division_fiscale_views.xml',
        'views/res_partner_views.xml',
        'views/res_company_views.xml',
        'report/sale_order_report_templates.xml',
        'report/account_move_report_templates.xml',
        'report/external_layout_standard.xml',
    ],
    'installable': True,
    'application': False,
}
