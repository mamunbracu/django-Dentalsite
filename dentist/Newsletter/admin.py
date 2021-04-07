from django.contrib import admin
from Newsletter.models import NewsletterUser
# Register your models here.

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email','subscribe_date',)

admin.site.register(NewsletterUser,NewsletterAdmin)