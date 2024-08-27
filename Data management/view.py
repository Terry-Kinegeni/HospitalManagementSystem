from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import viewsets

router = DefaultRouter()
router.register(r'patients', viewsets.PatientViewSet, basename='patients')
router.register(r'doctors', viewsets.DoctorViewSet, basename='doctors')
router.register(r'appointments', viewsets.AppointmentViewSet, basename='appointments')
router.register(r'medical-reports', viewsets.MedicalRecordViewSet, basename='medical-reports')