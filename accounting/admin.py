from django.contrib import admin
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin
from .models import Price, Tarif
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
from import_export.resources import ModelResource


class PriceResource(ModelResource):
    class Meta:
        model = Price

    def for_delete(self, row, instance):
        return self.fields['parametrs', 'tarif', 'grade'].clean(row) == ''


class TarifAdmin(SummernoteModelAdmin):
    fields = ['title', 'activity', 'minimal_price', 'currency', 'unit', 'description', 'param_1', 'param_2', 'param_3', 'param_4', 'update_date']
    list_display = ('title', 'description', 'activity', 'update_date',)
    list_filter = ('activity', 'currency',)
    readonly_fields = ["minimal_price", "update_date"]


class PriceAdmin(ImportExportMixin, admin.ModelAdmin):
    fields = ['parametrs', 'tarif', 'grade', ('salary', 'currency',), 'price_date', 'activity']
    list_display = ('parametrs', 'tarif', 'grade', 'salary', 'currency', 'price_date', 'activity',)
    list_filter = ('activity', 'grade', 'tarif',)
    resource_class = PriceResource

admin.site.register(Price, PriceAdmin)
admin.site.register(Tarif, TarifAdmin)
