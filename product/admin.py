from django.contrib import admin

from product.models import Category, Product, Delivery, ProductItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'created_at']
    search_fields = ['name', 'description', 'barcode']
    list_filter = ['created_at', 'category__name']
    date_hierarchy = 'created_at'


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone']
    search_fields = ['name', 'phone']
    list_filter = ['address']


@admin.register(ProductItem)
class ProductItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'quantity', 'deliver', 'created_at']
    list_filter = ['created_at', 'deliver', 'product', 'expired']
    search_fields = ['product__name', 'deliver__name']
    date_hierarchy = 'created_at'


