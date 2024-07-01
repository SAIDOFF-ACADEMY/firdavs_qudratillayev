from modeltranslation.translator import register, TranslationOptions
from .models import Settings, Page


@register(Page)
class PageTranslationOptions(TranslationOptions):
    fields = ('slug', 'title', 'content')


@register(Settings)
class SettingsTranslationOptions(TranslationOptions):
    fields = ('contact_telegram', 'contact_phone', 'longitude', 'latitude', 'locations_text', 'working_horse_start',
              'working_horse_end', 'telegram_bot')
