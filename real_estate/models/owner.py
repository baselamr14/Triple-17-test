from odoo import models, fields, api


class Owner(models.Model):
    _name = 'owner'
    _description = 'owner'

    name = fields.Char()
    phone=fields.Char()
    address=fields.Char()
    property_ids=fields.One2many('property','owner_id')