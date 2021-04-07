from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from Newsletter.forms import NewsletterForm
from Newsletter.models import NewsletterUser
from django.contrib import messages
# Create your views here.

def UserNewsletter(request):
    form = NewsletterForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)

        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.success(request, "This email is already subscribe the newsletter!!!")
        else:
            instance.save()
            messages.success(request, "Subscription successfully.We will give you our best!!!")
            return HttpResponseRedirect(reverse('dental:index'))
    return render(request, 'Newsletter/subscribe.html', context={'form':form})
  
