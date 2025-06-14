# product/management/commands/serve_grpc.py
import grpc
from concurrent import futures
from django.core.management.base import BaseCommand
from grpc_server import product_pb2, product_pb2_grpc

from product_app.models import Product


class ProductServiceServicer(product_pb2_grpc.ProductServiceServicer):
    def GetProduct(self, request, context):
        # Here you can access Django models
        # For example: Product.objects.get(id=request.product_id)
        product = Product.objects.get(id=request.id)
        return product_pb2.ProductResponse(
            id=request.id,
            name=product.name,
            price=product.price
        )


class Command(BaseCommand):
    help = "Starts the gRPC server"

    def handle(self, *args, **options):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        product_pb2_grpc.add_ProductServiceServicer_to_server(
            ProductServiceServicer(), server
        )
        server.add_insecure_port('[::]:50051')
        self.stdout.write(self.style.SUCCESS("Starting gRPC server on port 50051..."))
        server.start()
        server.wait_for_termination()
