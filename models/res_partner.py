from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date, datetime, timedelta

import logging
_logger = logging.getLogger(__name__)

class ResPartnter(models.Model):
    _name="res.partner"
    _inherit="res.partner"

    # _name="ext.res.partner"
    # _inherit="res.partner"

    feedback_ids = fields.One2many('customer.feedback', 'customer_id', readonly=True,
                                   string="Feedbacks")





