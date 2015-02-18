from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin

from membernews.models import MemberNewsEntry


class MemberNewsEntryAdmin(SummernoteModelAdmin):
    list_display = ['title', 'pub_date']

admin.site.register(MemberNewsEntry, MemberNewsEntryAdmin)
