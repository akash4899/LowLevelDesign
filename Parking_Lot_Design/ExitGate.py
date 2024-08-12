from Ticket import Ticket
from CostComputation import CostComputation

class ExitGate:
    def __init__(self, psm_factory):
        self.psm_factory = psm_factory

    def remove_vehicle(self, ticket):
        psm = self.psm_factory.get_parking_manager(ticket.vehicle.type, None)
        psm.remove_vehicle()

    def cost_computation(self, ticket):
        pass
