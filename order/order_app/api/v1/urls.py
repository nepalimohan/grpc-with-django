from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from django.urls import include

router = DefaultRouter()
router.register('orders', views.OrderViewSet, basename='orders')

urlpatterns = [
    path('', include(router.urls))
]
