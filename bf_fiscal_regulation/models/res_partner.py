# -*- coding: utf-8 -*-
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = "res.partner"

    ifu = fields.Char(
        string='N° IFU',
        help="Identifiant Financier Unique. Obligatoire pour les entreprises, "
             "facultatif pour les contacts individuels.",
    )
    rccm = fields.Char(
        string='N° RCCM',
        help="Registre du Commerce et du Crédit Mobilier. Obligatoire pour les "
             "entreprises, facultatif pour les contacts individuels.",
    )
    regime_impot_id = fields.Many2one(
        'bf.regime.impot', string="Régime d'imposition",
    )
    division_fiscale_id = fields.Many2one(
        'bf.division.fiscale', string="Division fiscale",
    )

    @api.constrains('ifu', 'rccm', 'company_type')
    def _check_bf_fiscal_identification(self):
        """IFU/RCCM sont obligatoire pour les entreprises mais facultatif
        pour les contacts individuels, même lorsqu'ils sont définis/modifiés
        en dehors de la vue du formulaire (import, API, XML-RPC, ...)."""
        for partner in self:
            if partner.company_type != 'company':
                continue
            missing = []
            if not partner.ifu:
                missing.append(_("N° IFU"))
            if not partner.rccm:
                missing.append(_("N° RCCM"))
            if missing:
                raise ValidationError(_(
                    "%(partner)s est une entreprise contact: %(fields)s "
                    "doit être rempli.",
                    partner=partner.display_name,
                    fields=", ".join(missing),
                ))
