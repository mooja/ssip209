from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Page


class PageAdmin(SummernoteModelAdmin):
    list_display = ['title']

admin.site.register(Page, PageAdmin)
