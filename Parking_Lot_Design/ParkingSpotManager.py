from abc import ABC

class ParkingSpotManager(ABC):
    def __init__(self, parking_spots):
        self.parking_spots = parking_spots

    def find_parking_space(self):
        pass

    def add_parking_space(self):
        pass

    def remove_parking_space(self):
        pass

    def park_vehicle(self, vehicle):
        pass

    def remove_vehicle(self, vehicle):
        pass