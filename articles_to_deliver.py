from article import Article

class ArticlesToDeliver:
    def __init__(self):
        self.articleList = []

    def init_articles(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                
                parts = line.strip().split(', ')
                
                if len(parts) == 3:
                    name = parts[0]
                    try:
                        truck_type = int(parts[1].split(': ')[1])  
                        destination = parts[2]
                        
                        if truck_type in [1, 2]:
                            article = Article(name, truck_type, destination)
                            self.articleList.append(article)
                        else:
                            print(f"TruckType incorrect pour l'article '{name}': doit être 1 ou 2, trouvé {truck_type}")
                    except (IndexError, ValueError) as e:
                        print(f"Ligne mal formatée ignorée: '{line.strip()}' - Erreur: {e}")
                else:
                    print(f"Ligne mal formatée ignorée: '{line.strip()}'")

    def get_articles(self):
        return self.articleList
