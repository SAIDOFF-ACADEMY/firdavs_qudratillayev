from rest_framework import generics
from product.models import Product, FreeProduct
from product.landing.serializers import ProductLandingSerializer, FreeProductLandingSerializer


class ProductLandingView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductLandingSerializer


# class FreeProductLandingView(generics.ListAPIView):
#     queryset = FreeProduct.objects.all()
#     serializer_class = FreeProductLandingSerializer
