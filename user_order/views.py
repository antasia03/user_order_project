from .serializers import (
    CustomUserSerializer,
    OrderSerializer,
    OrderCreationSerializer
)
from .models import CustomUser, Order
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return OrderCreationSerializer
        else:
            return OrderSerializer
