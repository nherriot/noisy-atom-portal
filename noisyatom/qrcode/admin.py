from django.contrib import admin
from .models import QRcode

# Registering category and products

class QRcodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'primary_url', 'secondary_url')
    search_fields = ('name', 'slug', 'primary_url', 'secondary_url')
    ordering = ('name', 'slug', 'created_at')

admin.site.register(QRcode, QRcodeAdmin)
