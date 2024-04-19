"""
Master: The master program/process is responsible for running and communicating with the other components in the system. When running the master program, the following parameters should be provided as input:
number of mappers (M)
number of reducers (R)
number of centroids (K)
number of iterations for K-Means (Note: program should stop if the algorithm converges before)
Other necessary information (This should be reasonable. Please check with us - if you are not sure!)

"""
import random
import grpc
from concurrent import futures
import json
import time
import mapper_pb2
import mapper_pb2_grpc
import reducer_pb2
import reducer_pb2_grpc
import time
from logger import Logger

MAPPERS = 1
CENTROIDS = 1
REDUCERS = 1
ITERATIONS = 20
DataForMappers = []
Centroids = []



def split_data_indexes(data):
    data_size = len(data)
    points_per_mapper = data_size // MAPPERS
    indexes = []

    # code such that both start and end indexes are included
    start_index = 0
    for _ in range(MAPPERS - 1):
        end_index = start_index + points_per_mapper
        indexes.append((start_index, end_index))
        start_index = end_index+1
    indexes.append((start_index, data_size))
    return indexes

def GenerateCentroids(input_data, k):
    random.shuffle(input_data)
    centroids = input_data[:k]
    return centroids

def call_mappers(Centroids,DataForMappers,logger):
    partitionForReducers = {}
    for i in range(MAPPERS):
        port = 50051+i
        channel = grpc.insecure_channel('localhost:'+str(port))
        stub = mapper_pb2_grpc.MapperServiceStub(channel)
        
        request = mapper_pb2.centroidUpdateRequest(points = DataForMappers[i],centroids=json.dumps(Centroids))
        logger.log("Sending data to mapper at port "+str(port))
        
        response = stub.ReceiveCentroid(request)
        logger.log("Recieved partition from mapper at port "+str(port))

        partition = json.loads(response.partition)
        for key in partition:
            if key in partitionForReducers:
                partitionForReducers[key].extend(partition[key])
            else:
                partitionForReducers[key] = partition[key]
    return partitionForReducers

def call_reducers(partitions,logger):
    updated_centroids = []
    for i in range(REDUCERS):
        port = 50061 + i
        channel = grpc.insecure_channel('localhost:'+str(port))
        stub = reducer_pb2_grpc.ReducerServiceStub(channel)
        id = str(i+1)
        
        request = reducer_pb2.partitionRequest(partition=json.dumps(partitions[id]), id=id)
        logger.log("Sending partitions to reducer at port " + str(port))

        response = stub.RecievePartition(request)
        logger.log("Recieved updated centroids from reducer at port " + str(port))
        
        centroids = json.loads(response.updated_centroid)

        logger.log_reducers(f"Reducer {id} updated centroids {centroids}", id)
        updated_centroids.append(centroids)
    
    logger.log("Updated centroids received from reducer at port "+str(port)+" are "+str(updated_centroids))
    return updated_centroids



if __name__ == "__main__":
    logger = Logger("dump.txt", "centroids.txt", "Reducers")
    with open("points.txt", "r") as file:
        input_data = [list(map(float, line.strip().split(','))) for line in file]
    
    Centroids = GenerateCentroids(input_data, CENTROIDS)
    logger.log("Initial (random) Centroids are "+str(Centroids))
    DataForMappers = split_data_indexes(input_data)

    for i in range(ITERATIONS):
        logger.log("\n")
        logger.log("ITERATION "+str(i))
        partitions = call_mappers(Centroids,DataForMappers,logger)
        updated_Centroids = call_reducers(partitions,logger)
        logger.log_centroids(updated_Centroids,i)
        if updated_Centroids == Centroids:
            print("Converged after ",i," iterations")
            break
        else:
            Centroids = updated_Centroids

        print("updated centroids after ",i," iterations ",Centroids)

    logger.log("Converged after "+str(i)+" iterations")
    print("Final centroids are ",Centroids)



    

   

    

   
