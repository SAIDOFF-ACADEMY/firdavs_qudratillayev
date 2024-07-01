from django.contrib import admin
from .models import GalleryPhoto, Page, Settings
from modeltranslation.admin import TranslationAdmin


@admin.register(Settings)
class SettingsAdmin(TranslationAdmin):
    def has_add_permission(self, request):
        if Settings.objects.exists():
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        if Settings.objects.exists():
            return False


@admin.register(Page)
class PageAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'content')
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(GalleryPhoto)
