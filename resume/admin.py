from django.contrib import admin
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin
from .models import Order

class OrderAdmin(SummernoteModelAdmin):
    fields = [('name', 'surname',), ('last_date', 'status',), ('country', 'company',), ('phone', 'telegram',), 'email', 'text', 'conformation', 'order_date']
    list_display = ('email', 'telegram', 'phone', 'company', 'country', 'status', 'last_date', 'order_date',)

    readonly_fields = ('order_date', 'conformation',)
admin.site.register(Order, OrderAdmin)
