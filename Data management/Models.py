from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    # ... other patient information fields

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    # ... other doctor information fields

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    treatment_plan = models.TextField()
    # ... other medical record fields

class Allergy(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    allergen = models.CharField(max_length=255)
    severity = models.CharField(max_length=255)  # e.g., mild, moderate, severe