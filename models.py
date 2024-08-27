from django.db import models


class patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    patient_number = models.CharField(max_length=15)
    Email_address = models.EmailField()
    Id_number = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()

    def __str__  (self):
        return f'{self.first_name} {self.last_name}'