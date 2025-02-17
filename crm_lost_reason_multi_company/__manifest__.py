# Copyright (C) 2025 - Today: Sylvain LE GAL (http://www.grap.coop)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Crm Lost Reason Multi Company",
    "summary": """
        This module adds support for multi company on crm lost reasons.""",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "author": "GRAP, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/multi-company",
    "depends": ["crm"],
    "data": ["views/crm_lost_reason.xml", "security/ir_rule.xml"],
    "installable": True,
}
