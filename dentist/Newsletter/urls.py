from django.urls import path
from Newsletter import views 

app_name = 'Newsletter'
urlpatterns = [
    
    path('subscribe/', views.UserNewsletter, name='subscribe'),
    

]