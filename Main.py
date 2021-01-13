from Graph import Graph
from Algorithms import Algorithm
import math
import time
import logging
import os

os.remove("logfile.log")
logging.basicConfig(filename="logfile.log", level=logging.INFO)

graph = Graph(9)
graph.remove_connections(0.2)
model = Algorithm(graph)
start_time = time.time()
costs1 = model.BFS()
times = [time.time() - start_time]
start_time = time.time()
costs2 = model.DFS()
times.append(time.time() - start_time)
start_time = time.time()
costs3 = model.NN()
times.append(time.time() - start_time)

logging.info("finish")
logging.info(f'Shortest BFS: {min(costs1)}')
logging.info(f'Shortest DFS: {min(costs2)}')
logging.info(f'Shortest NN: {min(costs3)}')
logging.info(f'Time BFS: {times[0]}')
logging.info(f'Time DFS: {times[1]}')
logging.info(f'Time NN: {times[2]}')
logging.info(f'costs lenght BFS: {len(costs1)}')
logging.info(f'costs lenght DFS: {len(costs2)}')
logging.info(f'All paths BFS: {costs1}')
logging.info(f'All paths DFS: {costs2}')
