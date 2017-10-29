from django.contrib import admin
from .models import Product, Category, ProductItem

# Registering category and products

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active')
    search_field = ('name', 'slug')
    ordering = ('name', 'slug','created_at','updated_at')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'brand', 'sku', 'price', 'quantity')
    search_fields = ('name', 'slug', 'sku')
    ordering = ('name', 'slug', 'sku', 'price', 'created_at', 'updated_at')

class ProductItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'brand', 'sku', 'sale_price', 'product')
    search_fields = ('name', 'slug', 'brand', 'product')
    ordering = ('name', 'slug', 'sku', 'brand', 'product')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductItem, ProductItemAdmin)
