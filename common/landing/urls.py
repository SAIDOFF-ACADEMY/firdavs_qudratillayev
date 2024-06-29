from django.urls import path
from common.landing.view import PageLandingView, GalleryPhotoLandingView, SettingsLendingView

urlpatterns = [
    path('page/', PageLandingView.as_view(), name='landing'),
    path('settings/', SettingsLendingView.as_view(), name='settings'),
    path('gallery/', GalleryPhotoLandingView.as_view(), name='gallery'),
]
