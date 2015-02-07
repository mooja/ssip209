from django.contrib import admin

from membernews.models import MemberNewsEntry


class MemberNewsEntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date']

admin.site.register(MemberNewsEntry, MemberNewsEntryAdmin)
