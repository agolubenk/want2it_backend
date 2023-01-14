from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Contact, Emplouee

class ContactAdmin(SummernoteModelAdmin):
    list_display = ('title', 'name', 'telegram', 'phone', 'email', 'address',)
    search_fields = ['title', 'name', 'telegram', 'phone', 'email']
    filter = ['title',]


class EmploueeAdmin(SummernoteModelAdmin):
    list_display = ('title', 'name', 'activity',)
    search_fields = ['title', 'name',]
    filter = ['title', 'activity',]

admin.site.register(Contact, ContactAdmin)
admin.site.register(Emplouee, EmploueeAdmin)





