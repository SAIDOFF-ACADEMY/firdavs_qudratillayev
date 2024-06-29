from django.urls import path
from product.landing.view import ProductLandingView

urlpatterns = [
    path('product/', ProductLandingView.as_view(), name='landing'),
    # path('product/free', FreeProductLandingView.as_view(), name='free'),

]
