import mapper_pb2_grpc
import mapper_pb2
import grpc
import json
import argparse
import sys
import os
import master_pb2_grpc, master_pb2
from concurrent import futures
import reducer_pb2
import reducer_pb2_grpc

class Reducer(reducer_pb2_grpc.ReducerServiceServicer):

    def __init__(self):
        self.intermediate_data = []
        self.output = {}

    def reduce(self):

        inputData = self.intermediate_data
        x = 0
        y = 0
        for point in inputData:
            x += point[0]
            y += point[1]
        x = x / len(inputData)
        y = y / len(inputData)
       # self.output[self.id] = [x, y]
        output = [x, y]
        return output


    def RecievePartition(self, request, context):
        partitions = json.loads(request.partition)
        self.intermediate_data = partitions
        updated_centroids = self.reduce()
        print("Sent updated centroids to master")
        
        return reducer_pb2.updated_centroids(updated_centroid = json.dumps(updated_centroids))

def server(id):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    reducer_pb2_grpc.add_ReducerServiceServicer_to_server(Reducer(), server)
    port = 50061 + id 
    server.add_insecure_port('[::]:'+str(port))
    print(f"Reducer {args.id} started on port {port}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--id", help="The id of the mapper", type=int)
    args = parser.parse_args()
    if args.id == None:
        print("id needed")
        sys.exit(-1)

    server(id=args.id)


