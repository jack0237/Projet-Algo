from graph import Graph
from articles_to_deliver import ArticlesToDeliver

class Main:
    def __init__(self, cities_file, articles_file):
        self.graph = Graph()
        self.articles_to_deliver = ArticlesToDeliver()
        self.cities_file = cities_file
        self.articles_file = articles_file

    def run(self):
        self.graph.init_graph(self.cities_file)

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

        self.articles_to_deliver.init_articles(self.articles_file)

        print("\nArticles to deliver:")
        for article in self.articles_to_deliver.get_articles():
            print(f"- {article.name} (Truck Type: {article.truck_type}) to {article.destination}")

if __name__ == "__main__":
    main_program = Main('cities.txt', 'articles.txt')
    main_program.run()
