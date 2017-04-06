from django.contrib import admin
from .models import CustomerAddress, Company

# Registering category and products

class CustomerAddressAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'country')
    search_field = ('name', 'postal_code', 'city')
    ordering = ('name', 'address_line1', 'postal_code', 'city', 'country', 'modified_date')

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'company_number', 'company_url', 'vat')
    search_fields = ('name', 'company_number', 'company_url')
    ordering = ('name', 'company_number', 'company_url', 'vat', 'description', 'modified_date')


admin.site.register(CustomerAddress, CustomerAddressAdmin)
admin.site.register(Company, CompanyAdmin)


