from truck import Truck
from node import Node

class Fleet:
    def __init__(self, starting_point=None):
        self.truckList = []
        self.starting_point = starting_point

    def init_fleet(self, file_path):
        with open(file_path, 'r') as file:
            starting_point_name = file.readline().strip()
            self.starting_point = Node(starting_point_name)

            for line in file:
                parts = line.strip().split(', ')
                if len(parts) == 2:
                    truck_id = parts[0].split()[1]
                    truck_type = int(parts[1].split(': ')[1])
                    
                    truck = Truck(truck_id, truck_type)
                    self.truckList.append(truck)

    def __repr__(self):
        return f"Fleet(starting_point={self.starting_point}, truckList={self.truckList})"
