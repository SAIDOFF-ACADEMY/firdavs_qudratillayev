from rest_framework import generics
from .models import Page, GalleryPhoto
from .serializers import PageSerializer, GalleryPhotoSerializer


class PageList(generics.ListAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class PageCreate(generics.CreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class PageUpdate(generics.UpdateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class PageDelete(generics.DestroyAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class GalleryPhotosCreate(generics.CreateAPIView):
    queryset = GalleryPhoto.objects.all()
    serializer_class = GalleryPhotoSerializer


class GalleryPhotoList(generics.ListAPIView):
    queryset = GalleryPhoto.objects.all()
    serializer_class = GalleryPhotoSerializer


class GalleryPhotoDelete(generics.DestroyAPIView):
    queryset = GalleryPhoto.objects.all()
    serializer_class = GalleryPhotoSerializer
