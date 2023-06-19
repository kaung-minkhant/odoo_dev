from odoo import models, api, fields,_
from ksuid import ksuid

class StudentModel(models.Model):
    _name = 'lte.student'
    _description = 'lte student model'
    _inherit = ['mail.thread']
    _sql_constraints = [

        ('student_id', 'unique (student_id)', 'Student ID must be unique!')

    ]
    _res_name = 'name'
    
    name = fields.Char('Student Name', tracking=True)
    ref = fields.Char('Reference Sequence')
    age = fields.Integer('Age', tracking=True)
    nick_name = fields.Char('Student Nickname', tracking=True)
    parent = fields.Char('Parent Name', tracking=True)
    gender = fields.Selection(string='Gender', selection=[
        ('male', 'Male'),
        ('female', 'Female')
    ], tracking=True)
    student_id = fields.Char('Student ID', default=lambda self: _("New"), readonly=True)
    student_ksuid = fields.Char('Student KSUID')
    active = fields.Boolean('Active', default=True)
    
    @api.model_create_multi
    def create(self, vals):
        for val in vals:
            original = str(ksuid())
            original_upper = original.upper()
            original_id = original_upper[-6:]
            val['student_ksuid'] = original
            val['student_id'] = original_id
            
        return super(StudentModel, self).create(vals)

    def name_get(self):
        res = []
        for record in self:
            if record.parent:
                res.append((record.id, "%s - %s -%s" % (record.student_id, record.name, record.parent)))
            else:
                res.append((record.id, "%s - %s" % (record.student_id, record.name)))


        return res