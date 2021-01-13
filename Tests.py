from Graph import Graph
from Algorithms import Algorithm
import math
import time
import logging
import os

os.remove("logfile.log")
logging.basicConfig(filename="logfile.log", level=logging.INFO)

graph = Graph(9)
graph.remove_connections(0)
model = Algorithm(graph)
result = model.Dijkstra()
print(result)
