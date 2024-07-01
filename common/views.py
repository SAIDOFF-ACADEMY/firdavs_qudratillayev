from rest_framework import generics
from .models import Page, GalleryPhoto
from .serializers import PageSerializer, GalleryPhotoSerializer
from rest_framework.permissions import IsAdminUser

class PageList(generics.ListAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [IsAdminUser]


class PageCreate(generics.CreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [IsAdminUser]



class PageUpdate(generics.UpdateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [IsAdminUser]


class PageDelete(generics.DestroyAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [IsAdminUser]


class GalleryPhotosCreate(generics.CreateAPIView):
    queryset = GalleryPhoto.objects.all()
    serializer_class = GalleryPhotoSerializer
    permission_classes = [IsAdminUser]


class GalleryPhotoList(generics.ListAPIView):
    queryset = GalleryPhoto.objects.all()
    serializer_class = GalleryPhotoSerializer
    permission_classes = [IsAdminUser]


class GalleryPhotoDelete(generics.DestroyAPIView):
    queryset = GalleryPhoto.objects.all()
    serializer_class = GalleryPhotoSerializer
    permission_classes = [IsAdminUser]
