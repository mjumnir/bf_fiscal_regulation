Burkina Faso - Fiscal Regulation (IFU / RCCM)
==============================================

This addon adds the fiscal identification required by Burkina Faso's
Direction Générale des Impôts (DGI) to contacts, companies, and to the
Sale Order and Customer Invoice reports: N° IFU, N° RCCM, régime
d'imposition, and division fiscale.

Main features
-------------

* Company contacts require an IFU and an RCCM number; individual
  contacts are exempt.
* Companies (``res.company``) always carry an IFU and an RCCM number.
* Two configuration lists, Régime d'imposition and Division fiscale,
  can be maintained from Accounting/Invoicing ▸ Configuration without
  touching the code.
* The Sale Order report and the Customer Invoice report display the
  seller's IFU, RCCM, tax regime, and fiscal division, and the
  customer's IFU/RCCM whenever they are filled in.
* The IFU/RCCM requirement is enforced both in the form views and at
  the ORM level, so it also applies to records created through import,
  the API, or XML-RPC.

The addon depends on ``base``, ``contacts``, ``sale``, and ``account``,
and does not alter any accounting or fiscal computation logic.
