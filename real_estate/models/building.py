from string import digits
import logging

from odoo import models, fields, api
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__) # ← fix

class Building(models.Model):
    _name = 'building'
    _description = 'building' # optional but recommended
    _inherit=['mail.thread','mail.activity.mixin']

    no = fields.Integer()
    code=fields.Char()
    description = fields.Text()
    _rec_name='code'
    active=fields.Boolean(default=True)
