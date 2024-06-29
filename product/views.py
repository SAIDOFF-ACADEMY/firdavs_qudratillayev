from django.shortcuts import render
from rest_framework import generics
from .models import Product, FreeProduct
from .serializers import ProductSerializer, FreeProductSerializer


class ProductCreateApiView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateApiView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDeleteApiView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class FreeProductList(generics.ListAPIView):
    queryset = FreeProduct.objects.all()
    serializer_class = FreeProductSerializer
