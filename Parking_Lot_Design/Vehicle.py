from VehicleType import VehicleType

class Vehicle:
    def __init__(self, number, type: VehicleType):
        self.number = number
        self.type = type

    def get_type(self):
        return self.type