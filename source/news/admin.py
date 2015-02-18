from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from news.models import NewsEntry

class NewsEntryAdmin(SummernoteModelAdmin):
    list_display = ['title', 'pub_date']

admin.site.register(NewsEntry, NewsEntryAdmin)
