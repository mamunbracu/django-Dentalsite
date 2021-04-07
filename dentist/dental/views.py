from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request,'dental/index.html', context={})

def contact(request):
	return render(request, 'dental/contact.html', {})

def about(request):
	return render(request, 'dental/about.html', {})

def pricing(request):
	return render(request, 'dental/pricing.html', {})

def service(request):
	return render(request, 'dental/service.html', {})


