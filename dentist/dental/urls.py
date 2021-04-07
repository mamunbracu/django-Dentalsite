
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'dental'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name="about"),
	path('pricing/', views.pricing, name="pricing"),
	path('service/', views.service, name="service"),


]
