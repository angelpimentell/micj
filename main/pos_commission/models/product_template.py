from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    commission = fields.Float(digits=(3, 2))

    @api.model
    def create(self, vals):
        self.verify_commission_value(vals)
        return super().create(vals)

    def write(self, vals):
        self.verify_commission_value(vals)
        return super().write(vals)

    @api.onchange('commission')
    def onchange_commission(self):
        self.verify_commission_value()

    def verify_commission_value(self, vals=None):
        if vals is None:
            vals = {}

        commission = vals.get('commission', self.commission)

        if commission > 100:
            raise UserError(_("Commission percentage couldn't be greater than 100."))
