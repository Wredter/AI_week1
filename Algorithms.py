import random
import queue
from Graph import Tree, calc_cost_form_leaf, get_path, calc_cost_form_leaf_without_returning
import logging
import copy


class Algorithm:
    metrics = []

    def __init__(self, graph, symmetrical=True):
        self.graph = graph
        self.symmetrical = symmetrical
        self.tree = Tree(random.choice(self.graph.all_nodes), self.graph)

    def BFS(self):
        costs = []
        que = [copy.deepcopy(self.tree.root)]
        first = True
        while que:
            node = que.pop(0)
            logging.info(f'Current path {get_path(node)}')
            neighbours = self.tree.create_connected_leafs(node)
            for neighbour in neighbours:
                que.append(neighbour)
            if node.name == self.tree.root.name and not first:
                costs.append(calc_cost_form_leaf_without_returning(node, symmetrical=self.symmetrical))
            first = False
        return costs

    def DFS(self):
        costs = []
        que = [copy.deepcopy(self.tree.root)]
        first = True
        first_dist = False
        while que:
            node = que.pop()
            logging.info(f'Current path {get_path(node)}')
            if node.name == self.tree.root.name and not first:
                costs.append(calc_cost_form_leaf_without_returning(node, symmetrical=self.symmetrical))
                first_dist = True
            elif first_dist:
                part_cost = calc_cost_form_leaf_without_returning(node, symmetrical=self.symmetrical)
                if part_cost > min(costs):
                    continue
            neighbours = self.tree.create_connected_leafs(node)
            for neighbour in neighbours:
                que.append(neighbour)
            first = False
        return costs






