from VehicleType import VehicleType
from CarSpotManager import CarSpotManager
from MotorcycleSpotManager import MotorcycleSpotManager
class ParkingManagerFactory:
    def get_parking_manager(self, vehicle_type, parking_spots):
        if vehicle_type == VehicleType.CAR:
            return CarSpotManager(parking_spots)
        elif vehicle_type == VehicleType.MOTORCYCLE:
            return MotorcycleSpotManager(parking_spots)
        else:
            raise Exception("Invalid Vehicle Type.")