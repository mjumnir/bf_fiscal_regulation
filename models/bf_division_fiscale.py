# -*- coding: utf-8 -*-
from odoo import fields, models


class BfDivisionFiscale(models.Model):
    _name = 'bf.division.fiscale'
    _description = "Division fiscale"
    _order = 'name'

    name = fields.Char("Division fiscale", required=True)
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('name_uniq', 'unique(name)', "Cette division fiscale existe déjà."),
    ]
