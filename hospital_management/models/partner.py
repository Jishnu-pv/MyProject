from odoo import api, fields, models


class PatientDob(models.Model):
    _inherit = 'res.partner'

    dob = fields.Date(string="DOB")
