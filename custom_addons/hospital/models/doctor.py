from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _description = "Hospital Doctor Records"
    _inherit = ['mail.thread']
    _rec_name = "ref"

    name = fields.Char(string="Doctor Name", required=True, tracking=True)
    gender = fields.Selection(string="Gender",
                                selection=[('m',"Male"), ('f',"Female"), ('o',"Other")],
                                tracking=True
                              )
    ref = fields.Char(string="Reference", default=lambda self: _("NEW"), readonly=True)
    active = fields.Boolean('Active', default=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.doctor.sequence');
        return super(HospitalDoctor, self).create(vals_list)

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, "%s - %s" % (record.ref, record.name)))
        return result