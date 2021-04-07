

from django.urls import path
from . import views

app_name = 'Appointment'
urlpatterns = [
    
    path('appointment/', views.appointment, name='appointment'),
    path('contact/', views.contact, name='contact'),

]
