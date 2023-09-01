from django.contrib import admin

from catalog.models import Product, Category, Version


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'overview')


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Version)
class Version(admin.ModelAdmin):
    list_display = ('product', 'version_number', 'version_name', 'is_current')
