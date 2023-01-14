from django.contrib import admin
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin
from .models import Order

class OrderAdmin(SummernoteModelAdmin):
    fields = ['name', 'surname', 'status', 'last_date', 'telegram', 'email', 'company', 'country', 'phone', 'text', 'order_date']
    list_display = ('email', 'telegram', 'phone', 'company', 'country', 'status', 'last_date', 'order_date',)

admin.site.register(Order, OrderAdmin)
