from django.contrib import admin
from .models import GalleryPhoto, Page, Settings


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Settings.objects.exists():
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        if Settings.objects.exists():
            return False


admin.site.register(GalleryPhoto)
admin.site.register(Page)
