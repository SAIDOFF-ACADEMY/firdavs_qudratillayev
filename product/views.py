from rest_framework.permissions import IsAdminUser
from rest_framework import generics
from .models import Product, FreeProduct
from .serializers import ProductSerializer, FreeProductSerializer


class ProductCreateApiView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]



class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]


class ProductUpdateApiView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]


class ProductDeleteApiView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]


class FreeProductList(generics.ListAPIView):
    queryset = FreeProduct.objects.all()
    serializer_class = FreeProductSerializer
    permission_classes = [IsAdminUser]
