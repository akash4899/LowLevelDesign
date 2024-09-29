from enum import Enum

class BookingStatus(Enum):
    BOOKED = 'Booked'
    CANCELED = 'Canceled'

class Booking:
    def __init__(self, id, flight, seat, passenger, price):
        self.id = id
        self.flight = flight
        self.seat = seat
        self.passenger = passenger
        self.status = BookingStatus.BOOKED
        self.price = price
        #print("here2")

    def cancel(self):
        self.status = BookingStatus.CANCELED

    def get_booking_id(self):
        return self.id

    def get_flight(self):
        return self.flight

    def get_seat(self):
        return self.seat

    def get_passenger(self):
        return self.passenger

    def get_price(self):
        return self.price

    def get_status(self):
        return self.status