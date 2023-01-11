from django.contrib import admin
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin
from .models import Blog

class BlogAdmin(SummernoteModelAdmin):
    fields = ['title', 'post', 'previeww', 'image', 'blog_date', 'draft']
    summernote_fields = ('post',)
    list_display = ('title', 'preview', 'blog_date', 'draft')
    list_filter = ('draft',)

    readonly_fields = ["preview", "previeww"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 28px;">')

    def previeww(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 160px;">')

admin.site.register(Blog, BlogAdmin)
