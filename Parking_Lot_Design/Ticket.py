from ParkingSpot import ParkingSpot
from Vehicle import Vehicle
from datetime import datetime
class Ticket:
    def __init__(self):
        self.entry_time = None
        self.vehicle = None
        self.parking_spot = None

    def set(self, vehicle, parking_spot):
        self.entry_time = datetime.now()
        self.vehicle = vehicle
        self.parking_spot = parking_spot

    def get_vehicle(self):
        return self.vehicle

    def get_parking_spot(self):
        return self.parking_spot