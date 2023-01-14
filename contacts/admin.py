from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Contact

class ContactAdmin(SummernoteModelAdmin):
    list_display = ('title', 'name', 'telegram', 'phone', 'email', 'address',)
    search_fields = ['title', 'name', 'telegram', 'phone', 'email']
    filter = ['title',]



admin.site.register(Contact, ContactAdmin)





