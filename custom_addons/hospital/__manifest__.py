{
    'name': 'Hospital Management System',
    'author': 'Polar',
    'application': True,
    'license': 'LGPL-3',
    'depends' : ['mail'],
    'data' : [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/patient.xml',
        'views/female_patient.xml',
        'views/doctor.xml',
        'views/appointment.xml',
        'views/menus.xml',
        'report/patient_record_report.xml'
    ]
}