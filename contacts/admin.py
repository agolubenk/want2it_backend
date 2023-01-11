from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Contacts

class ContactsAdmin(SummernoteModelAdmin):
    list_display = ('title', 'telegram', 'phone', 'email', 'address', 'default_status')
    search_fields = ['title', 'phone', 'email']
    filter = ['default_status',]



admin.site.register(Contacts, ContactsAdmin)





