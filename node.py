from edge import Edge

class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []

    def add_edge(self, edge):
        self.edges.append(edge)

    def has_edge_to(self, node_name):
        return any(edge.to_node.name == node_name for edge in self.edges)
