import random
import queue
import numpy as np
from Graph import Tree, calc_cost_form_leaf, get_path, calc_cost_form_leaf_without_returning, Leaf, check_parent_names
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

    def Dijkstra(self, leaf, visited):
        que = [copy.deepcopy(leaf)]
        costs = {}
        not_visited = list(self.graph.get_all_nodes_names())
        for node in visited:
            if node in not_visited:
                not_visited.remove(node)
        for node in not_visited:
            costs[node] = None, np.inf
        costs[self.tree.root.name] = copy.deepcopy(self.tree.root), 0
        while not_visited:
            node = que.pop()
            neighbours = self.tree.create_connected_leafs(node)
            not_visited.remove(node.name)
            for n in visited:
                if n in node.get_connection_names():
                    wisited_l = node.get_connected_node(n)
                    neighbours.remove(wisited_l)
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
            return create_tree_from_dict(costs)

    def Dijkstra_search(self):
        que = [copy.deepcopy(self.tree.root)]
        node = que.pop()
        visited = []
        all_nodes = list(self.graph.get_all_nodes_names())
        while que:
            part_tree = self.Dijkstra(node, visited)
            part_tree.d_connections = dict(sorted(part_tree.d_connections.items(), key=lambda item: item[1][1]))
            que2 = [part_tree]
            while que2:
                node = que.pop()
                logging.info(f'Current path {get_path(node)}')
                visited.append(node.name)
                if not bool(node.d_connections):
                    connections = node.get_connection_names()
                    parents = check_parent_names(node)
                    if not visited:
                        visited = get_path(node)
                        que.append(node)
                    if get_path(node) == all_nodes:
                        if self.tree.root.name in node.get_connection_names():
                            return [calc_cost_form_leaf_without_returning(node, symmetrical=self.symmetrical)]
                d_connections = node.get_d_connected_leafs()
                for d_connection in d_connections:
                    que.append(d_connection)


def create_tree_from_dict(dictionary):
    not_found = True
    for key in dictionary:
        _leaf, _cost = dictionary[key]
        parent = _leaf.parent
        #print(_leaf.d_connections is parent.d_connections)
        while parent is not None:
            parent.d_connections[_leaf.name] = (_leaf, _cost)
            _leaf = _leaf.parent
            parent = _leaf.parent
            if parent is None and not_found:
                root = _leaf
                not_found = False
    return root






