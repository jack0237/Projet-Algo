from node import Node
from edge import Edge

class Graph:
    def __init__(self):
        self.nodesList = {}

    def init_graph(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split(', ')
                start_node = parts[0]
                
                if start_node not in self.nodesList:
                    self.nodesList[start_node] = Node(start_node)

                i = 1
                while i < len(parts) - 1:
                    destination_node = parts[i]
                    distance = int(parts[i + 1])

                    if start_node != destination_node:
                        if destination_node not in self.nodesList:
                            self.nodesList[destination_node] = Node(destination_node)

                        edge = Edge(self.nodesList[start_node], self.nodesList[destination_node], distance)
 
                        if not self.nodesList[start_node].has_edge_to(destination_node):
                            self.nodesList[start_node].add_edge(edge)
                        if not self.nodesList[destination_node].has_edge_to(start_node):
                            reverse_edge = Edge(self.nodesList[destination_node], self.nodesList[start_node], distance)
                            self.nodesList[destination_node].add_edge(reverse_edge)
                    
                    i += 2

    def get_nodes(self):
        return list(self.nodesList.keys())

    def get_edges(self, node_name):
        if node_name in self.nodesList:
            return [(edge.to_node.name, edge.distance) for edge in self.nodesList[node_name].edges]
        return None
