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
        new_node = Node(len(self.all_nodes))
        new_node.randomize(self.min_range, self.max_range, self.z_range)
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

    def __init__(self, name, x=0, y=0, z=0):
        self.name = name
        self.x = x
        self.y = y
        self.z = z

    def randomize(self, min_range, max_range, z_range):
        print("Randomizing node")
        self.x = random.randint(min_range, max_range)
        self.y = random.randint(min_range, max_range)
        self.z = random.randint(0, z_range)
        print(self.x, self.y, self.z)

    def create_all_connections(self, nodes):
        self.connections = list(nodes)

    def create_connection(self, node):
        self.connections.append(node)

    def get_conection_names(self):
        names = []
        for node in self.connections:
            names.append(node.name)
        return names


class Leaf(Node):
    def __init__(self, node, parent):
        super().__init__(name=node.name, x=node.x, y=node.y, z=node.z)
        self.connections = node.connections
        self.parent = parent
        self.cost_to_get_to = 0

    def cost_to_travel(self, symmetrical=True):
        start = [self.parent.x, self.parent.y, self.parent.z]
        finish = [self.x, self.y, self.z]
        _sum = 0
        for i in range(3):
            partial = (start[i]-finish[i])**2
            _sum += partial
        cost = math.sqrt(_sum)
        if symmetrical:
            return cost
        else:
            if start[2] > finish[2]:
                return cost * 0.9
            else:
                return cost * 1.1

    def cost_to_travel_to_any(self, goal, symmetrical=True):
        finish = [goal.x, goal.y, goal.z]
        start = [self.x, self.y, self.z]
        if goal.name not in self.get_conection_names():
            print("Panie przecie tam nie da się stąd dojechać")
        _sum = 0
        for i in range(3):
            partial = (start[i]-finish[i])**2
            _sum += partial
        cost = math.sqrt(_sum)
        if symmetrical:
            return cost
        else:
            if start[2] > finish[2]:
                return cost * 0.9
            else:
                return cost * 1.1


class Tree:
    def __init__(self, root):
        self.root = Leaf(root, None)
        self.create_leafs(self.root)

    def create_leafs(self, leaf):
        children = []
        for child in leaf.connections:
            parents = check_parent_names(leaf)
            if child.name in parents:
                continue
            new_leaf = Leaf(child, leaf)
            self.create_leafs(new_leaf)
            children.append(new_leaf)
        leaf.connections = children


def calc_cost_form_leaf_without_returning(leaf, symmetrical=True):
    parent = leaf.parent
    cost = 0
    while parent is not None:
        cost += leaf.cost_to_travel(symmetrical)
        parent = parent.parent
    return cost


def calc_cost_form_leaf(leaf, goal, symmetrical=True):
    parent = leaf.parent
    cost = leaf.cost_to_travel_to_any(goal)
    while parent is not None:
        cost += leaf.cost_to_travel(symmetrical)
        parent = parent.parent
    return cost


def check_parent_names(leaf):
    parent = leaf.parent
    parents = []
    while parent is not None:
        parents.append(parent.name)
        parent = parent.parent
    return parents


def get_path(leaf):
    parent = leaf.parent
    parents = [leaf.name]
    while parent is not None:
        parents.append(parent.name)
        parent = parent.parent
    return parents
