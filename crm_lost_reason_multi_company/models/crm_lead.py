# Copyright (C) 2025 - Today: Sylvain LE GAL (http://www.grap.coop)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class CrmLead(models.Model):
    _inherit = "crm.lead"

    lost_reason_id = fields.Many2one(check_company=True)
