from odoo import models, api, fields, _
from ksuid import ksuid

class ClassModel(models.Model):
    _name = 'lte.class'
    _description = 'lte class model'
    _inherit = ['mail.thread']
    _sql_constraints = [

        ('class_id', 'unique (class_id)', 'Class ID must be unique!')

    ]

    name = fields.Char('Class Name', tracking=True)
    description = fields.Text('Class Description', tracking=True)
    class_code = fields.Char('Class Short Code', tracking=True)
    class_id = fields.Char('Class ID', default=lambda self: _("New"), readonly=True)
    active = fields.Boolean('Active', default=True)

    @api.model_create_multi
    def create(self, vals):
        for val in vals:
            original = str(ksuid())
            original_upper = original.upper()
            original_id = original_upper[-6:]
            val['class_id'] = original_id
        return super(ClassModel, self).create(vals)
