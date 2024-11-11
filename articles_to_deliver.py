from article import Article

class ArticlesToDeliver:
    def __init__(self):
        self.articleList = []

    def init_articles(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split(', ')
                
                # Vérifie qu'il y a bien trois parties pour chaque ligne
                if len(parts) == 3:
                    try:
                        name = parts[0]
                        truck_type = int(parts[1].split(': ')[1])  # Assure que c'est un nombre entier (1 ou 2)
                        destination = parts[2]
                        
                        # Crée l'objet Article et l'ajoute à la liste
                        article = Article(name, truck_type, destination)
                        self.articleList.append(article)
                    except (IndexError, ValueError) as e:
                        print(f"Ligne mal formatée ignorée: '{line.strip()}' - Erreur: {e}")
                else:
                    print(f"Ligne mal formatée ignorée: '{line.strip()}'")
                    
    def get_articles(self):
        return self.articleList
