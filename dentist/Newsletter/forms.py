from django import forms

from Newsletter.models import NewsletterUser

class NewsletterForm(forms.ModelForm):
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={'placeholder':'Enter Email'}))
    class Meta:
        model = NewsletterUser
        fields = ['email']

        def clean_email(self):
            email = self.cleaned_data.get('email')
            return email