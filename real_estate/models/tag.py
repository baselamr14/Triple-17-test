from odoo import models, fields, api


class Tag(models.Model):
    _name = 'tag'
    _description = 'tag'

    name = fields.Char()
