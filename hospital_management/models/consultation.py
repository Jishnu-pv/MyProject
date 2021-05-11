from AptUrl.Helpers import _

from odoo import api, fields, models
import datetime


class HospitalConsultation(models.Model):
    _name = "hospital.consultation"
    _rec_name = "tocken_no"
    _description = "Hospital Op"
    patient_card = fields.Many2one(
        'hospital.patient', ondelete='set null', string='Patients Card', )
    con_id = fields.Selection([('o', 'OP'), ('i', 'IP'), ], string="Consultation Type")
    tocken_no = fields.Many2one(
        'hospital.ticket', ondelete='set null', string='Tocken No', )
    #tocken_no = fields.Char(string='Tocken Number', related='patient_card.tocken_no')
    doctor = fields.Many2one(string="Doctor", related='tocken_no.doctor')
    department = fields.Many2one(string="Department", related='doctor.department_id')
    date = fields.Date(string="Date", compute='calculate_date')
    disease = fields.Many2one('desease.patient', string='disease')
    Diagnose = fields.Text(string="Diagnose")
    appoinment_line = fields.One2many('hospital.line', 'cons_id', ondelete='set null')

    @api.depends("patient_card")
    def calculate_date(self):
        today_date = datetime.date.today()
        self.date = today_date
        print("today", today_date)

    @api.onchange('patient_card')
    def change_domain(self):
        for rec in self:
            print("hereee", rec.patient_card)
            return {'domain': {'tocken_no': [('patient_card', '=', rec.patient_card.id)]}}


class HospitalConsultationLines(models.Model):
    _name = "hospital.line"
    _description = "Hospital Op"

    patient_card = fields.Many2one(
        'hospital.ticket', ondelete='set null', string='Patients Card', )

    medicine = fields.Text(string='Medicine')
    dose = fields.Char(string='Dose')
    days = fields.Integer(string='Days')
    description = fields.Char(string='Description')
    cons_id = fields.Many2one('hospital.consultation', string='consult_id')





class Hospital(models.Model):
    _name = "desease.patient"
    _rec_name = 'disease'
    _description = "Hospital patient"
    disease = fields.Char(string='disease ', required=True)
