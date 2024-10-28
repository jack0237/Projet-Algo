import networkx as nx

def create_graph(fichier):
    graphe = nx.Graph()

    with open(fichier, 'r') as f:
        for ligne in f:
            elements = ligne.strip().split(', ') 
            ville_source = elements[0] 
            for i in range(1, len(elements) - 1, 2):
                ville_adj = elements[i] 
                temps = int(elements[i + 1])
                graphe.add_edge(ville_source, ville_adj, weight=temps)

    return graphe

def afficher_graphe(graphe):
    print("Villes (nœuds) :")
    print(graphe.nodes())

    print("\nConnexions (arêtes) avec temps de trajet :")
    for u, v, data in graphe.edges(data=True):
        print(f"{u} -- {v}, temps: {data['weight']} minutes")
 
graphe = create_graph(cities.txt)
afficher_graphe(graphe)
