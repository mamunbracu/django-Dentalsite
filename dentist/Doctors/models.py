from django.db import models

# Create your models here.

class DoctorsList(models.Model):
    image = models.ImageField(upload_to='doctors_pics')
    name = models.CharField(max_length=40)
    expert = models.CharField(max_length=100)
    experience = models.CharField(max_length=50)
