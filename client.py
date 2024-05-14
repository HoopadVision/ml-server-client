import grpc
from grpc_backend import image_pb2 as pb
from grpc_backend import image_pb2_grpc as rpc



class Client:
    def __init__(self, addr):
        self.channel = grpc.insecure_channel(addr)
        self.stub = rpc.requestserviceStub(self.channel)

    def request_start(self, text):
        request = pb.Request(byte=text)
        response = self.stub.Start(request)
        return response.embed

# if __name__ == "__main__":
#     client = Client("localhost:50051")
#     response = client.request_start("hello")
#     print("Response from server:", response)
