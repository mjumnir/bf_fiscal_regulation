# -*- coding: utf-8 -*-
from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    ifu = fields.Char(string='N° IFU', required=True, help="IFU")
    rccm = fields.Char(string='N° RCCM', required=True, help="RCCM")
    regime_impot_id = fields.Many2one(
        'bf.regime.impot', string="Régime d'imposition",
    )
    division_fiscale_id = fields.Many2one(
        'bf.division.fiscale', string="Division fiscale",
    )
