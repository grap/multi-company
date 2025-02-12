# Copyright (C) 2025 - Today: Sylvain LE GAL (http://www.grap.coop)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class CrmLostReason(models.Model):
    _inherit = "crm.lost.reason"

    company_id = fields.Many2one(
        comodel_name="res.company",
        string="Company",
        index=True,
        help="Specific company that uses this lost reason. "
        "Other companies will not be able to see or use it.",
        default=lambda self: self.env.company,
    )
