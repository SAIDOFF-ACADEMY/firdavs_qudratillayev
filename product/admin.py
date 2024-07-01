from django.contrib import admin
from .models import Product, FreeProduct
from modeltranslation.admin import TranslationAdmin


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('name', 'content', 'price')
    readonly_fields = ['created_at', 'updated_at']


@admin.register(FreeProduct)
class FreeProductAdmin(TranslationAdmin):
    list_display = ('product', 'count')
    readonly_fields = ['created_at', 'updated_at']
