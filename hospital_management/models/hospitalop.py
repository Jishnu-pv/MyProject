from AptUrl.Helpers import _

from odoo import api, fields, models
import datetime


class HospitalOpTicket(models.Model):
    _name = "hospital.ticket"
    _inherit = ['mail.thread.cc',
                'mail.activity.mixin']
    _description = "Hospital Op"
    #_rec_name = 'patient_card'
    _rec_name = 'tocken_no'

    patient_card = fields.Many2one(
        'hospital.patient', ondelete='set null', string='Patients Card', )
    _patients_name = fields.Many2one("hr.employee.base", string="names")
    name = fields.Char(string='Name', related='patient_card.patient_id.name', )
    age = fields.Integer(string="Age", related='patient_card.age')
    dob = fields.Date(string="DOB", related='patient_card.dob1')
    gender = fields.Selection(string="Gender", related="patient_card.gender")
    blood_group = fields.Selection(string="Blood Group", related="patient_card.blood_group")
    doctor = fields.Many2one('hr.employee', ondelete='set null', string="Doctors")
    department = fields.Many2one(string="Department", related='doctor.department_id')
    company_id = fields.Many2one("res.company", default=lambda self: self.env.company)
    currency_id = fields.Many2one("res.currency", string="Currency", related='company_id.currency_id', readonly=True)
    job = fields.Char(string="Gender", related="doctor.job_title")
    date = fields.Date(string="Date" , compute='calculate_date')
    tocken_no = fields.Char(string='Tocken Number', required=True, copy=False, readonly=True, index=True,
                            default=lambda self: _('New'))
    fee = fields.Integer(string='Fee', currency_field='currency_id', related='doctor.fee')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('op', 'OP'),
    ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')

    @api.model
    def create(self, vals):
        if vals.get('tocken_no', _('New')) == _('New'):
            vals['tocken_no'] = self.env['ir.sequence'].next_by_code('hospital.sequence.op', ) or _('New')
        result = super(HospitalOpTicket, self).create(vals)
        return result

    def action_confirm(self):
        for rec in self:
            rec.state = 'op'

    @api.depends("dob")
    def calculate_date(self):
        today_date = datetime.date.today()
        self.date = today_date
        print("today", today_date)

    @api.onchange('tocken_no')
    def change_domain(self):
        for rec in self:
            return {'domain': {'doctor': [('job_title', '=', 'Doctor')]}}

    def action_register_payment(self):
        ''' Open the account.payment.register wizard to pay the selected journal entries.
        :return: An action opening the account.payment.register wizard.
        '''
        return {
            'name': _('Register Payment'),
            'res_model': 'account.payment.register',
            'view_mode': 'form',
            'context': {
                'active_model': 'account.move',
                'active_ids': self.ids,
            },
            'target': 'new',
            'type': 'ir.actions.act_window',
        }


class HospitalOpTicket1(models.Model):
    _inherit = 'hospital.ticket'
    _name = "hospital.op"
    _description = "Hospital Op"
    _rec_name = 'tocken_no'
