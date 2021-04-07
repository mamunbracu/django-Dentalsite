from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from Appointment.forms import AppointmentForm, ContactForm
#messsage
from django.contrib import messages

# Create your views here.

def contact(request):
    formC = ContactForm()
    if request.method == 'POST':
        formC = ContactForm(request.POST)

        if formC.is_valid():
            formC.save()
            messages.success(request, "Your message is successfull! We will Contact you soon!!!")
            return HttpResponseRedirect(reverse('Appointment:contact'))
    return render(request, 'Appointment/contact.html', context={'formC':formC})

def appointment(request):
    form = AppointmentForm()

    if request.method == 'POST':

        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your booking successfully! We will let you kmow about your booking!!!")
            return HttpResponseRedirect(reverse('Appointment:appointment'))

    return render(request, 'Appointment/appointment.html', context={'form':form})