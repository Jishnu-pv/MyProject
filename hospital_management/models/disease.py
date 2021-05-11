import datetime
from datetime import date

from AptUrl.Helpers import _

from odoo import api, fields, models


class Hospital2(models.Model):
    _name = "hospital.disease"
    _description = "Hospital patient"
    disease = fields.Char(string='Disease ', required=True)
