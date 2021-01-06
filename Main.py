from Graph import Graph
from Algorithms import Algorithm
import math


graph = Graph(5)
graph.remove_connections(0)
model = Algorithm(graph)
costs = model.BFS()

print("finish")
print(f'Najkrutsza: {min(costs)}')
