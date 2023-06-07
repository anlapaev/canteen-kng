from django.contrib import admin

from products.models import Basket, Product, ProductCategory


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description', 'image', ('price', 'quantity'), 'stripe_product_price_id', 'category')
    search_fields = ('name',)
    ordering = ('-name',)


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    fields = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    readonly_fields = ['created_timestamp']
    fields = ('product', 'quantity', 'created_timestamp')
    extra = 0
