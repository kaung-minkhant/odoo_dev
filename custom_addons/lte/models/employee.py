from odoo import fields, api, models, _
from ksuid import ksuid


class EmployeeModel(models.Model):
    _name = 'lte.employee'
    _description = 'lte employee model'
    _inherit = ['mail.thread']

    name = fields.Char(string="Employee Name", tracking=True)
    age = fields.Integer(string="Age", tracking=True)
    gender = fields.Selection(string="Gender", selection=[
        ('male', "Male"),
        ('female', 'Female')
    ], tracking=True)
    employee_id = fields.Char(string="Employee ID", default=lambda self: _("New"), readonly=True)
    active = fields.Boolean('Active', default=True)

    @api.model_create_multi
    def create(self, vals):
        for val in vals:
            original = str(ksuid())
            original_upper = original.upper()
            original_id = original_upper[-6:]
            val['employee_id'] = original_id
        return super(EmployeeModel, self).create(vals)