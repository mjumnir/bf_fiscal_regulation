# -*- coding: utf-8 -*-
from odoo import fields, models


class BfRegimeImpot(models.Model):
    _name = 'bf.regime.impot'
    _description = "Régime d'imposition"
    _order = 'name'

    name = fields.Char("Régime d'imposition", required=True)
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('name_uniq', 'unique(name)', "Ce régime fiscal existe déjà."),
    ]
