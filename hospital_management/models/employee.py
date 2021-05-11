from odoo import api, fields, models


class PatientDob(models.Model):
    _inherit = 'hr.employee'

    fee = fields.Integer(string="FEE")
