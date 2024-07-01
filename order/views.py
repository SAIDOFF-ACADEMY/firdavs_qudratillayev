from .models import Order
from .serializers import OrderSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

class OrderList(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]
