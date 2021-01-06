import random
import queue
from Graph import Tree, calc_cost_form_leaf, get_path


class Algorithm:
    metrics = []

    def __init__(self, graph, symmetrical=True):
        self.graph = graph
        self.symmetrical = symmetrical
        self.tree = Tree(random.choice(self.graph.all_nodes))

    def BFS(self):
        costs = []
        que = [self.tree.root]

        while que:
            node = que.pop(0)
            print(f'Current path {get_path(node)}')
            neighbours = node.connections
            for neighbour in neighbours:
                if len(neighbour.connections) == 0:
                    costs.append(calc_cost_form_leaf(neighbour, self.tree.root))
                que.append(neighbour)
        return costs





