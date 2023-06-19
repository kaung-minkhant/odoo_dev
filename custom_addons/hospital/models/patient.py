from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient Records"
    _inherit = ['mail.thread']

    name = fields.Char(string="Patient Name", required=True, tracking=True)
    age = fields.Integer(string="Patient Age", tracking=True)
    is_child = fields.Boolean(string="Is Child?", tracking=True, compute='_compute_is_child', store=True)
    gender = fields.Selection(string="Gender",
                                selection=[('m',"Male"), ('f',"Female"), ('o',"Other")],
                                tracking=True
                              )
    capitalized_name = fields.Char(string="Capitalized Patient Name", compute='_compute_capatilized_name', store=True)
    ref = fields.Char(string="Reference", default=lambda self: _("NEW"), readonly=True)
    doctor_id = fields.Many2one(comodel_name='hospital.doctor',string="Doctor", tracking=True)
    active = fields.Boolean('Active', default=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
          vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence')
        return super(HospitalPatient, self).create(vals_list)

    @api.constrains('is_child','age')
    def _check_child_age(self):
        if self.is_child and self.age == 0:
            raise ValidationError(_("Age has to be recorded"))
    
    @api.depends('name')
    def _compute_capatilized_name(self):
        if self.name:
          self.capitalized_name = self.name.lower()
        else:
            self.capitalized_name = ''


    @api.depends('age')
    def _compute_is_child(self):
        if self.age <= 10:
            self.is_child = True
        else:
            self.is_child = False