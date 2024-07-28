from ParkingSpot import ParkingSpot
from Vehicle import Vehicle


class CarParkingSpot(ParkingSpot):
    def __init__(self, id):
        super.__init__(self, id)

    def price(self):
        return 10
