from django.urls import path
from .views import PageList, GalleryPhotoList, PageCreate, PageUpdate, PageDelete, GalleryPhotoDelete, \
    GalleryPhotosCreate

urlpatterns = [
    path('page/', PageList.as_view(), name='page-list'),
    path('page/create', PageCreate.as_view(), name='page-create'),
    path('page/update/<int:pk>', PageUpdate.as_view(), name='page-update'),
    path('page/delete/<int:pk>', PageDelete.as_view(), name='page-delete'),
    path('photo/', GalleryPhotoList.as_view(), name='photo-list'),
    path('photo/create/', GalleryPhotosCreate.as_view(), name='photo-create'),
    path('photo/delete/', GalleryPhotoDelete.as_view(), name='photo-delete'),
]
