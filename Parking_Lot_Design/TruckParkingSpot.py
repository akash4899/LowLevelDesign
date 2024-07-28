from Vehicle import Vehicle
from ParkingSpot import ParkingSpot

class TruckParkingSpot(ParkingSpot):
    def __init__(self):
        super().__init__(self)

    def price(self):
        return 20