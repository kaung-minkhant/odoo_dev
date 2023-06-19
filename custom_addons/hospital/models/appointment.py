from odoo import api, fields, models, _

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _description = "Hospital Appointment Records"
    _inherit = ['mail.thread']
    _rec_name = 'patient_id'

    patient_id = fields.Many2one('hospital.patient', string='Patient')
    appointment_time = fields.Datetime('Appointment Time', default=fields.Datetime.now())
    booking_date = fields.Date('Booking Date', default=fields.Date.today())
    gender = fields.Selection(string="Gender",
                                related='patient_id.gender'
                              )

   