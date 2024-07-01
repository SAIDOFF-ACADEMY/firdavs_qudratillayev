from modeltranslation.translator import register, TranslationOptions
from .models import Product, FreeProduct


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'content')


@register(FreeProduct)
class FreeProductTranslationOptions(TranslationOptions):
    fields = ('product', 'count', 'free_products')
