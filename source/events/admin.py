from django.contrib import admin
from .models import SSIPEvent, SSIPOccurrence, Location


class SSIPOccurrenceInline(admin.TabularInline):
    model = SSIPOccurrence
    extra = 1


class SSIPEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_type', 'description')
    list_filter = ('event_type', )
    search_fields = ('title', 'description')
    inlines = [SSIPOccurrenceInline]


class LocationAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


admin.site.register(SSIPEvent, SSIPEventAdmin)
admin.site.register(Location)
