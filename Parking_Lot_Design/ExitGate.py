

class ExitGate:
    def __init__(self, psm_factory):
        self.psm_factory = psm_factory

    def remove_vehicle(self, ticket):
        psm = self.psm_factory.get_parking_manager(ticket.vehicle.type, None)
        psm.remove_vehicle()

