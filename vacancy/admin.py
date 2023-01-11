from django.contrib import admin
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin
from .models import Vacancy
from .forms import ColorForm

class VacancyAdmin(SummernoteModelAdmin):
    fields = ['title', 'color', 'text', 'salary_from', 'salary_to', 'currency', 'grade', 'stack', 'benefits', 'vacancy_date', 'activity']
    summernote_fields = ('text', 'benefits',)
    list_display = ('title', 'color', 'salary_from', 'salary_to', 'currency', 'grade', 'vacancy_date', 'activity',)
    list_filter = ('activity', 'grade',)
    form = ColorForm

admin.site.register(Vacancy, VacancyAdmin)
