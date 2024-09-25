from reservation import Reservation
class Customer:
    def __init__(self, name, contact_number):
        self.name = name
        self.contact_number = contact_number
        self.reservations = []
        self.orders = []

    def view_menu(self, menu):
        pass

    def place_order(self, menu_item):
        pass

    def make_reservation(self, reservation_id, datetime):
        new_reservation = Reservation(reservation_id, datetime)
        self.reservations.append(new_reservation)
        return new_reservation