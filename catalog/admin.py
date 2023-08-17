from django.contrib import admin

from catalog.models import Product, Category


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'overview',)


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('id', 'name')
