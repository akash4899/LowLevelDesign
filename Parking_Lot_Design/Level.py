from ParkingSpotManager import ParkingSpotManager
from Vehicle import Vehicle
class Level:
    def __init__(self, id, parking_spot_managers):
        self.parking_spot_managers = parking_spot_managers
        self.id = id

    def park_vehicle(self, vehicle):
        if vehicle.type == 'car':
            self.parking_spot_managers[0]