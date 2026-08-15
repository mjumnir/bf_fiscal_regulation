# bf_fiscal_regulation

Odoo 17 module adding Burkina Faso (DGI) fiscal identification to
contacts, companies, and to the Sale Order / Customer Invoice reports.

## What's included
- `bf.regime.impot` / `bf.division.fiscale`: two small configuration
  models (menu under Invoicing/Accounting ▸ Configuration) so the
  regime and division lists are maintainable without code changes.
- `res.partner`: `ifu`, `rccm`, `regime_impot_id`, `division_fiscale_id`.
  `ifu`/`rccm` are required only when `company_type == 'company'`
  (individuals are exempt), enforced both in the form view and via a
  Python `@api.constrains` so it also holds for imports/API calls.
- `res.company`: same four fields, `ifu`/`rccm` always required.
- Sale Order report and Customer Invoice report: a small block showing
  the company's IFU/RCCM (+ regime/division) and, if filled in, the
  customer's IFU/RCCM.

## Before you install on an existing database
`res.company.ifu` / `rccm` are `required=True`. On a DB that already
has companies, Odoo will add the column without a hard NOT NULL
constraint (existing rows have no value yet) but the *form* will
require it going forward — fill in each company's IFU/RCCM right
after installing (Settings -> General Settings -> Companies), or the
Sale Order / Invoice reports will render an empty IFU/RCCM line until
you do.
