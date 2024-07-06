from django.urls import path
from .views import ProductList, FreeProductList, ProductCreateApiView, ProductUpdateApiView, ProductDeleteApiView


urlpatterns = [
    path('', ProductList.as_view(), name='product-list'),
    path('create/', ProductCreateApiView.as_view(), name='product-create'),
    path('product/update/<int:pk>', ProductUpdateApiView.as_view(), name='product-update'),
    path('product/delete/<int:pk>', ProductDeleteApiView.as_view(), name='product-delete'),
    path('free/', FreeProductList.as_view(), name='free-product-list'),
]
