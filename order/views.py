from .models import Order
from .serializers import OrderSerializer
from rest_framework import generics


class OrderList(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
