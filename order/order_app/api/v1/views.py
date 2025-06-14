from rest_framework import viewsets

from order_app.models import Order
from .serializers import OrderSerializer

from django.http import JsonResponse
from grpc_client.client import get_product

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

def order_detail_view(request):
    product_id = "1"
    print(type(product_id))
    product = get_product(product_id)
    print(product, 'asdfa')
    return JsonResponse({"order_id": 1, "product": {"id": product.id, "name": product.name, "price": product.price}})