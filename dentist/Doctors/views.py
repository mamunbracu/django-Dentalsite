from django.shortcuts import render
from Doctors.models import DoctorsList

# Create your views here.
def doctors(request):
    doctors_detailes = DoctorsList.objects.all()

    return render(request, 'Doctors/doctor.html', {'doctors_detailes':doctors_detailes})