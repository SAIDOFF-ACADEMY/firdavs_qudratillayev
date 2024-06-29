from rest_framework import serializers
from common.models import Page, GalleryPhoto, Settings


class PageLandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['slug', 'title', 'content']
        read_only_fields = ['created_at', 'updated_at']
        reg_name = 'LandingPage'


class GalleryPhotoLandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryPhoto
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
        reg_name = 'LandingPhoto'


class SettingsLendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ['contact_telegram', 'contact_phone', 'longitude', 'latitude', 'locations_text', 'working_horse_start',
                  'working_horse_end', 'telegram_bot']
        reg_name = 'LandingSettings'
