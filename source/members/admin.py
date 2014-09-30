from django.contrib import admin
from members.models import Member

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'email', 'homephone', 'cellphone']

admin.site.register(Member, MemberAdmin)
