# © 2016 Chafique DELLI @ Akretion
# © 2017 Today Mourad EL HADJ MIMOUNE @ Akretion
# 2020 Manuel Calero - Tecnativa
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Purchase and Invoice Allowed Product with product matrix",
    "summary": "This module allows to select only products that can be "
    "supplied by the vendor",
    "version": "17.0.1.0.0",
    "category": "Accounting & Finance",
    "website": "https://github.com/OCA/purchase-workflow",
    "author": "Nicolas JEUDY",
    "license": "AGPL-3",
    "depends": ["purchase", "purchase_allowed_product"],
    "data": [
        "views/purchase_order_views.xml",
    ],
    "installable": True,
}
