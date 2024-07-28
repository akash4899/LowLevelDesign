from ParkingManagerFactory import ParkingManagerFactory

class EntranceGate:
    def __init__(self, parking_spot_manager_factory):
        self.parking_spot_manager_factory = parking_spot_manager_factory

    def find_parking_space(self, vehicle_type, spots):
        psm = self.parking_spot_manager_factory.get_parking_manager(vehicle_type, spots)
        return psm.find_parking_space()

    def generate_ticket(self, vehicle, parking_spot):
        pass
