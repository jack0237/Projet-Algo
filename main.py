from graph import Graph
from articles_to_deliver import ArticlesToDeliver
from fleet import Fleet

class Main:
    def __init__(self, cities_file, articles_file, fleet_file):
        self.graph = Graph()
        self.articles_to_deliver = ArticlesToDeliver()
        self.cities_file = cities_file
        self.articles_file = articles_file
        self.fleet = Fleet()
        self.fleet_file = fleet_file

    def run(self):
        self.graph.init_graph(self.cities_file)

        # tests
        """print("Nodes in the graph:")
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
                print(f"No edges found for node {node_name}")"""

        self.articles_to_deliver.init_articles(self.articles_file)

        # tests
        """print("\nArticles to deliver:")
        for article in self.articles_to_deliver.get_articles():
            print(f"- {article.name} (Truck Type: {article.truck_type}) to {article.destination}")"""
        
        self.fleet.init_fleet(self.fleet_file)
        """print(f"Point de départ : {self.fleet.starting_point}")
        print("Flotte de camions initialisée :")
        for truck in self.fleet.truckList:
            print(truck)"""
        

if __name__ == "__main__":
    main_program = Main('cities.txt', 'articles.txt', 'fleet.txt')
    main_program.run()
