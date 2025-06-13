from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from django.urls import include

router = DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')


urlpatterns = [
    path('', include(router.urls))
]
