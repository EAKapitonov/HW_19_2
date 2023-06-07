from django.contrib import admin

from catalog.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',  'product_name', 'product_category_name', 'purchase_price',)
    list_filter = ('product_category_name',)
    search_fields = ('product_name', 'translator',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
