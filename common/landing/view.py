from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404
from common.landing.serializers import PageLandingSerializer, GalleryPhotoLandingSerializer, SettingsLendingSerializer
from common.models import Page, Settings, GalleryPhoto
import random


class PageLandingView(generics.GenericAPIView):
    queryset = Page.objects.all()
    serializer_class = PageLandingSerializer
    lookup_field = 'slug'

    def get_object(self):
        queryset = self.get_queryset()
        slug = self.kwargs.get('slug')
        return get_object_or_404(queryset, slug=slug)


class GalleryPhotoLandingView(generics.GenericAPIView):
    queryset = GalleryPhoto.objects.all()
    serializer_class = GalleryPhotoLandingSerializer

    def get(self, request, *args, **kwargs):
        gallery_photos = self.get_queryset()
        if gallery_photos.exists():
            random_photo = random.choice(gallery_photos)
            serializer = self.get_serializer(random_photo)
            return Response(serializer.data)
        return Response({"detail": "No photos available."}, status=404)


class SettingsLendingView(generics.ListAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsLendingSerializer
