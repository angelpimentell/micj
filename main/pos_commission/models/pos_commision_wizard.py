from odoo import models, fields, api
from datetime import datetime


class PosCommissionWizard(models.Model):
    _name = 'pos.commission.wizard'
    _description = 'Point of Sale Commission Report'

    start_date = fields.Date(required=True, default=datetime.today().replace(day=1))
    end_date = fields.Date(required=True, default=fields.Datetime.now)

    @api.onchange('start_date')
    def _onchange_start_date(self):
        if self.start_date and self.end_date and self.end_date < self.start_date:
            self.end_date = self.start_date

    @api.onchange('end_date')
    def _onchange_end_date(self):
        if self.end_date and self.end_date < self.start_date:
            self.start_date = self.end_date

    def print(self):
        data = {
            'name': 'Pedro',
        }
        return self.env.ref('pos_commission.report_payment_xls').report_action(self, data=data)
