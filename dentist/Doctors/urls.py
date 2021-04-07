
from django.urls import path
from . import views

app_name = 'Doctors'

urlpatterns = [
    
    path('doctors_list/', views.doctors, name='doctor'),


]
