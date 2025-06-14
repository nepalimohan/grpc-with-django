# server.py (in product_service/grpc_server/server.py)
import grpc
from concurrent import futures
from . import product_pb2, product_pb2_grpc

class ProductServiceServicer(product_pb2_grpc.ProductServiceServicer):
    def GetProductInfo(self, request, context):
        # Simulate DB fetch
        return product_pb2.ProductResponse(id=request.id, name="Test Product", price="99.99")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    product_pb2_grpc.add_ProductServiceServicer_to_server(ProductServiceServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()
