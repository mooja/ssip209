from django.contrib import admin

# Register your models here.
from news.models import NewsEntry

class NewsEntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date']

admin.site.register(NewsEntry, NewsEntryAdmin)
