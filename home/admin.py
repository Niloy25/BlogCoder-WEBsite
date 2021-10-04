from django.contrib import admin
from home.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'content']

# Register your models here.
admin.site.register(Contact, ContactAdmin)
