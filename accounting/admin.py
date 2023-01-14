from django.contrib import admin
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin
from .models import Price, Tarif

class TarifAdmin(SummernoteModelAdmin):
    fields = ['title', 'color', 'text', 'salary_from', 'salary_to', 'currency', 'grade', 'stack', 'benefits', 'vacancy_date', 'activity', 'hot']
    summernote_fields = ('text', 'benefits',)
    list_display = ('title', 'color', 'salary_from', 'salary_to', 'currency', 'grade', 'vacancy_date', 'activity',)
    list_filter = ('activity', 'grade', 'hot',)

class PriceAdmin(SummernoteModelAdmin):
    fields = ['title', 'color', 'text', 'salary_from', 'salary_to', 'currency', 'grade', 'stack', 'benefits', 'vacancy_date', 'activity', 'hot']
    summernote_fields = ('text', 'benefits',)
    list_display = ('title', 'color', 'salary_from', 'salary_to', 'currency', 'grade', 'vacancy_date', 'activity',)
    list_filter = ('activity', 'grade', 'hot',)

admin.site.register(Price, PriceAdmin)
admin.site.register(Tarif, TarifAdmin)
