# client.py (in order_service/grpc_client/client.py)
import grpc
from . import product_pb2, product_pb2_grpc

def get_product(product_id):
    with grpc.insecure_channel('localhost:50051') as channel:
    # with grpc.insecure_channel('product_service:50051') as channel:
        stub = product_pb2_grpc.ProductServiceStub(channel)
        print(type(product_id), 'req', product_id)
        request = product_pb2.ProductRequest(id=product_id)
        response = stub.GetProduct(request)
        return response