from django.test import TestCase
from .models import patient


class PatientModelTest(TestCase):
    def setUp(self):
        patient.objects.create(
            first_name="john",
            last_name="John",
            patient_number = "5556908",
            Email_address = "Johnjohn@gmail.com",
            id_number="38004002",
            phone_number ="0722678987",
            date_of_birth ="1997-01-01"
        )
    def test_patient_creation(self):
        patient = patient.objects.get(first_name="john")
        self.assertEqual(patient.last_name,"John")
        self.assertEqual(str(patient),"john John")
