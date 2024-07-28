from Vehicle import Vehicle
from VehicleType import VehicleType

class Car(Vehicle):
    def __init__(self, number):
        super.__init__(number, VehicleType.CAR)