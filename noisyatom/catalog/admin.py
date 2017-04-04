from django.contrib import admin
from .models import Product, Category, ProductItem

# Registering category and products

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductItem)
