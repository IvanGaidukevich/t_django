from django.contrib import admin
from catalog.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'in_stock', 'created_at', 'updated_at']
    list_editable = ['price', 'in_stock']
    list_filter = ['in_stock', 'price']


