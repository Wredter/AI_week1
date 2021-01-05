import numpy as np
import random
import math


class Graph:
    all_nodes = []
    min_range = 0
    max_range = 0
    z_range = 0
    num_of_all_connections = 0

    def __init__(self, number_of_nodes, min_range=-100, max_range=100, z_range=50):
        print("Creating graph")
        self.min_range = min_range
        self.max_range = max_range
        self.z_range = z_range
        self.num_of_all_connections = (number_of_nodes * (number_of_nodes - 1))/2
        for i in range(number_of_nodes):
            self.add_node()

    def add_node(self):
        new_node = Node(self.min_range, self.max_range, self.z_range, len(self.all_nodes))
        new_node.create_all_connections(self.all_nodes)
        for node in self.all_nodes:
            node.create_connection(new_node)
        self.all_nodes.append(new_node)

    def remove_connections(self, percent):
        to_remove = math.floor(self.num_of_all_connections * percent)
        while to_remove > 0:
            start_node = random.choice(self.all_nodes)
            if len(start_node.connections) <= 2:
                continue
            end_node = random.choice(start_node.connections)
            if len(end_node.connections) <= 2:
                continue
            start_node.connections.remove(end_node)
            end_node.connections.remove(start_node)
            to_remove -= 1


class Node:
    connections = []
    name = 0
    x = 0
    y = 0
    z = 0

    def __init__(self, min_range, max_range, z_range, name):
        print("Creating node")
        self.name = name
        self.x = random.randint(min_range, max_range)
        self.y = random.randint(min_range, max_range)
        self.z = random.randint(0, z_range)
        print(self.x, self.y, self.z)

    def create_all_connections(self, nodes):
        self.connections = list(nodes)

    def create_connection(self, node):
        self.connections.append(node)
