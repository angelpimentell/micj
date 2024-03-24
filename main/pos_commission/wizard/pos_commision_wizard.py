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

        orders = self.env['pos.order'].search([
            ('date_order', '<=', self.end_date),
            ('date_order', '>=', self.start_date),
            ('state', 'in', ['paid', 'done', 'invoiced']),
        ])

        user_data = {}

        for order in orders:
            user_id = order.partner_id.referrer_id.id

            if order.create_uid.id not in user_data:
                user_data[user_id] = 0

            for line in order.lines:
                commission = line.product_id.commission

                if commission and len(order.partner_id.referrer_id) > 0:
                    user_data[user_id] += line.product_id.list_price * commission / 100

        data = []

        for key, value in user_data.items():
            data.append(
                {
                    'name': self.env['res.users'].browse(key).name,
                    'amount': value,
                }
            )

        data = {
            'data': data
        }

        return self.env.ref('pos_commission.report_payment_xls').report_action(self, data=data)
