from odoo import models


class PartnerXlsx(models.AbstractModel):
    _name = 'report.pos_commission.report_payment_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        sheet = workbook.add_worksheet('COMISIONES')
        # sheet.right_to_left()
        # sheet.set_column(3, 3, 50)
        # sheet.set_column(2, 2, 30)
        sheet.write(0, 0, 'REFERIDO')
        sheet.write(0, 1, 'MONTO')

        for index, data in enumerate(data['data']):
            sheet.write(index + 1, 0, data['name'])
            sheet.write(index + 1, 1, data['amount'])
