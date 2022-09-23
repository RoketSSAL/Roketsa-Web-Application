from django.contrib import admin
from .models import MailingListUser, Mail

# Register your models here.

admin.site.register(MailingListUser)
admin.site.register(Mail)
