from django.contrib import admin
from .models import *

# Register your models here.

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email','message', 'status', 'note']
    readonly_fields = ['name','email', 'message']
    list_filter = ['status']
    list_display_links = ['status', 'name', 'note']
    search_fields = ['name', 'email',  'message', 'status', 'note']
    list_per_page = 20


admin.site.register(Blog_profile)
admin.site.register(ContactMessage, ContactMessageAdmin)