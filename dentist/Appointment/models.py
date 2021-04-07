from django.db import models

# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=30, blank=True)
    phone = models.TextField(blank=True)
    address = models.CharField(max_length=50, blank=True)
    appointment_time = models.CharField(max_length=50)
    appointment_date = models.CharField(max_length=30)
    message = models.TextField(max_length=260)
    

    def __str__(self):
        return self.name

class MessageUser(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    information = models.TextField(max_length=260)

    def __str__(self):
        return self.name