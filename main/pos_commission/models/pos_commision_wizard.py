from odoo import models, fields, api


class PosCommissionWizard(models.Model):
    _name = 'pos.commission.wizard'
    _description = 'Point of Sale Commission Report'

    def _default_start_date(self):
        """ Find the earliest start_date of the latests sessions """
        # restrict to configs available to the user
        config_ids = self.env['pos.config'].search([]).ids
        # exclude configs has not been opened for 2 days
        self.env.cr.execute("""
            SELECT
            max(start_at) as start,
            config_id
            FROM pos_session
            WHERE config_id = ANY(%s)
            AND start_at > (NOW() - INTERVAL '2 DAYS')
            GROUP BY config_id
        """, (config_ids,))
        latest_start_dates = [res['start'] for res in self.env.cr.dictfetchall()]
        # earliest of the latest sessions
        return latest_start_dates and min(latest_start_dates) or fields.Datetime.now()

    start_date = fields.Date(required=True, default=_default_start_date)
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
