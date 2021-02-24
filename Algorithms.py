import random
import queue
import numpy as np
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

    def NN(self):
        que = [copy.deepcopy(self.tree.root)]
        first = True
        first_dist = False
        while que:
            node = que.pop()
            logging.info(f'Current path {get_path(node)}')
            neighbours = self.tree.create_connected_leafs(node)
            if node.name == self.tree.root.name and not first:
                return [calc_cost_form_leaf_without_returning(node, symmetrical=self.symmetrical)]
            first = False
            costs = {}
            for neighbour in neighbours:
                costs[neighbour.name] = (calc_cost_form_leaf_without_returning(neighbour, symmetrical=self.symmetrical), neighbour)
            my_min = dict(sorted(costs.items(), key=lambda item: item[1]))
            for key in my_min:
                que.append(my_min[key][1])

    def Dijkstra(self):
        que = [copy.deepcopy(self.tree.root)]
        costs = {}
        not_visited = list(self.graph.get_all_nodes_names())
        for node in not_visited:
            costs[node] = None, np.inf
        costs[self.tree.root.name] = copy.deepcopy(self.tree.root), 0
        while not_visited:
            node = que.pop()
            neighbours = self.tree.create_connected_leafs(node)
            not_visited.remove(node.name)
            for neighbour in neighbours:
                tmp_cost = (calc_cost_form_leaf_without_returning(neighbour, symmetrical=self.symmetrical))
                _, curr_cost = costs[neighbour.name]
                if tmp_cost < curr_cost:
                    costs[neighbour.name] = (neighbour, tmp_cost)
            sub_costs = {key: costs[key] for key in not_visited}
            for key in sub_costs:
                _leaf, _cost = sub_costs[key]
                _min = np.inf
                if _cost < _min:
                    _min = _cost
                    min_leaf = _leaf
            que.append(min_leaf)
        return costs


def create_tree_from_dict(dictionary):
    return None





