from Vehicle import Vehicle
from VehicleType import VehicleType
from abc import ABC


class ParkingSpot(ABC):
    def __init__(self, id):
        self.id = id
        self.is_empty = True
        self.vehicle = None
        self.price = 0

    def is_available(self):
        return self.is_occupied

    def park_vehicle(self, vehicle):
        self.is_empty = False
        self.vehicle = vehicle

    def remove_vehicle(self):
        self.is_empty = True
        self.vehicle = None

    def get_parked_vehicle(self):
        return self.vehicle

    def get_spot_number(self):
        return self.id
