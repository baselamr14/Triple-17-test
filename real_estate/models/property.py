from string import digits
import logging

from odoo import models, fields, api
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__) # ← fix

class Property(models.Model):
    _name = 'property'
    _description = 'Property' # optional but recommended
    _inherit=['mail.thread','mail.activity.mixin']

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char(required=True)
    date_availability = fields.Date()
    selling_price = fields.Float()
    expected_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    active = fields.Boolean(default=True)
    diff=fields.Float(compute="_compute_diff")
    garden_orientation = fields.Selection([
        ('north','North'),
        ('south','South'),
        ('east','East'),
        ('west','West'),
    ])
    state=fields.Selection(
        [
            ('draft','Draft'),
            ('pending','Pending'),
            ('sold','Sold'),
            ('closed','Closed')
        ]
    )
    owner_id=fields.Many2one('owner')
    tag_ids=fields.Many2many('tag')
    owner_phone = fields.Char(related='owner_id.phone',readonly=0)
    owner_address = fields.Char(related='owner_id.address',readonly=0)
    Lines_ids=fields.One2many('property.line','property_id')
    _sql_constraints=[
        ('unique_name','unique("name")','This name already exits')

                    ]

    @api.constrains('bedrooms')
    def _check_bedrooms_greater_zero(self):
        for rec in self:
            if rec.bedrooms <= 0:   # ← disallow zero & negatives
                raise ValidationError("Please enter a valid number of bedrooms")

    @api.model_create_multi
    def create(self, vals_list):
        _logger.debug("inside create: %s", vals_list)
        res = super(Property, self).create(vals_list)
        return res

    # Correct write override
    def write(self, vals):
        _logger.debug("inside write: %s", vals)
        res = super(Property, self).write(vals)
        return res

    def unlink(self):
        _logger.debug("inside delete: ids=%s", self.ids)
        return super(Property, self).unlink()

    # Only override _search if you truly need to; if so, use the modern signature:
    # def _search(self, domain, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
    #     _logger.debug("inside _search, domain=%s ...", domain)
    #     return super()._search(domain, offset=offset, limit=limit, order=order, count=count,
    #                            access_rights_uid=access_rights_uid)

    def action_draft(self):
        self.write({'state': 'draft'})

    def action_pending(self):
        self.write({'state': 'pending'})

    def action_sold(self):
        self.write({'state': 'sold'})

    def action_closed(self):
        self.write({'state':'closed'})



    def _compute_diff(self):
        for rec in self:
            rec.diff=rec.expected_price - rec.selling_price

class PropertyLine(models.Model):
    _name='property.line'
    area=fields.Float()
    description=fields.Char()
    property_id=fields.Many2one('property')