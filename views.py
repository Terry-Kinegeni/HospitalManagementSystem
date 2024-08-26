from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import patient

def patient_list(request):
    patients = patient.objects.all()
    return render(request, 'patients/patient_list.html',{'patients':patients})

def patient_detail(request, pk):
    patient = get_object_or_404(patient, pk=pk)
    return render (request, 'patients/patient_detail.html', {'patient': patient})
