from graph import Graph

class Main:
    def __init__(self, file_path):
        self.graph = Graph()
        self.file_path = file_path

    def run(self):
        self.graph.init_graph(self.file_path)

        print("Nodes in the graph:")
        for node_name in self.graph.get_nodes():
            print(f"- {node_name}")

        print("\nEdges in the graph:")
        for node_name in self.graph.get_nodes():
            edges = self.graph.get_edges(node_name)
            if edges:
                print(f"Edges from {node_name}:")
                for to_node, distance in edges:
                    print(f"  - to {to_node}, distance: {distance} km")
            else:
                print(f"No edges found for node {node_name}")

if __name__ == "__main__":
    main_program = Main('cities.txt')
    main_program.run()