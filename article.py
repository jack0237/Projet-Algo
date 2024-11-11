class Article:
    def __init__(self, name, truck_type, destination):
        self.name = name
        self.truck_type = truck_type
        self.destination = destination

    def __repr__(self):
        return f"Article(name='{self.name}', truck_type='{self.truck_type}', destination='{self.destination}')"
