from AptUrl.Helpers import _

from odoo import api, fields, models


class HospitalAppoinment(models.Model):
    _name = "hospital.appoinment"
    _description = "Hospital appoinment"
    patient_card = fields.Many2one('hospital.patient', ondelete='set null', string='Patients Card', )
    patient_card1 = fields.Many2one('hospital.ticket', ondelete='set null', string='Patients Card', )
    tocken_no = fields.Many2one(
        'hospital.ticket', ondelete='set null', string='Tocken No', )
    name = fields.Char(string='Name', related='patient_card.patient_id.name', )
    doctor = fields.Many2one(string="Doctor", related='tocken_no.doctor')
    department = fields.Many2one(string="Department", related='doctor.department_id')
   # tocken_no = fields.Many2one(
        #'hospital.consultation', ondelete='set null', string='Tocken No', )
    #tocken_no = fields.Char(string='Tocken No', related='patient_card.tocken_no')
    date = fields.Date(string='Date', related="tocken_no.date")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('op', 'OP'),
        ('app', 'Appoinment')

    ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')

    op_count = fields.Integer(string='Invoice Count', compute='_get_op', readonly=True)

    def action_confirm(self):
        for rec in self:
            rec.state = 'app'

    def action_confirm1(self):
        print("iddd", self.id)

        return {
            'name': _('OP'),
            'domain': [('patient_card', '=', self.patient_card.id)],
            'view_type': 'form',
            'res_model': 'hospital.ticket',
            'view_id': 	'hospital_management.patientOp_form',
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }



    def action_conver_op(self):
        for rec in self:
            rec.state = 'op'
        _rec_name = 'op'
        print("iddd", self.id)
        return {

            'name': _('OP'),
            'view_type': 'form',
            'res_model': 'hospital.ticket',
            'view_mode': 'form',
            'type': 'ir.actions.act_window',
            'state': 'op',

        }


    @api.onchange('patient_card')
    def change_domain(self):

        for rec in self:
            print("hereee", rec.patient_card)
            return {'domain': {'tocken_no': [('patient_card', '=', rec.patient_card.id)]}}

        print('patient_card.tocken_no')

    @api.depends('tocken_no')
    def _get_op(self):
        count = 0
        for order in self:
            a = order.tocken_no
            count = count + 1
            print(a)
        #count = len(a)
        print(self)
        #count = self.patient_card.tocken_no
        #count = str(self.tocken_no)
        count = len(self.patient_card)
        self.op_count = count

