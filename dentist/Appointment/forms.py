from django import forms
from Appointment.models import Appointment, MessageUser

appointment_time = (
    ("Choose Your Time", "Choose Your Time"),
    ("1 pm to 3 pm", "1 pm to 3 pm"),
    ("3 pm to 5 pm", "3 pm to 5 pm"),
    ("5 pm to 7 pm", "5 pm to 7 pm"),
    ("7 pm to 9 pm", "7 pm to 9 pm"),
    
        
)
appointment_date = (
    ("Choose Your Date", "Choose Your Date"),
    ("Saturday", "Saturday"),
    ("Monday", "Monday"),
    ("Tuesday", "Tuesday"),
    ("Wednesday", "Wednesday"),
    ("Thursday", "Thursday"),
        
)
class AppointmentForm(forms.ModelForm):
    name = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder':'Enter Your Name'}))
    phone = forms.IntegerField(required=True, label="", widget=forms.TextInput(attrs={'placeholder':'Enter Phone Number'}))
    #email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={'placeholder':'Enter Email'}))
    address = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder':'Your Address'}))
    appointment_time = forms.ChoiceField(choices = appointment_time,label="") 
    appointment_date = forms.ChoiceField(choices = appointment_date,label="") 
    message = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder':'Your message'}))
    class Meta:
        model = Appointment
        fields = '__all__'


class ContactForm(forms.ModelForm):
    name = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder':'Enter Your Name'}))
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={'placeholder':'Enter Email'}))
    information = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder':'Your problem'}))

    class Meta:
        model = MessageUser
        fields = '__all__'