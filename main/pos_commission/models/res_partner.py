from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    referrer_id = fields.Many2one('res.users')
