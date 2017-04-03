from django.contrib import admin
from .models import Product, Category

# Registering category and products

admin.site.register(Product)
admin.site.register(Category)
