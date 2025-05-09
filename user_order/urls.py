from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls))
]
