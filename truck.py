class Truck:
    def __init__(self, truck_id, truck_type):
        self.truck_id = truck_id
        self.truckType = truck_type
        self.route = []
        self.articles_inside = []

    def add_article(self, article):
        self.articles_inside.append(article)
        print(f"Article {article.name} ajouté au {self.truck_id}")

    def remove_article(self, article):
        if article in self.articles_inside:
            self.articles_inside.remove(article)
            print(f"Article {article.name} retiré du {self.truck_id}")
        else:
            print(f"Article {article.name} non trouvé dans le {self.truck_id}")

    def __repr__(self):
        return f"Truck(id='{self.truck_id}', type={self.truckType}, route={self.route}, articles={self.articles_inside})"
