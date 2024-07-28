from Vehicle import Vehicle
from ParkingSpot import ParkingSpot

class MotorcycleParkingSpot(ParkingSpot):
    def __init__(self):
        super().__init__(self)

    def price(self):
        return 5