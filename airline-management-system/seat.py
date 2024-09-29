from enum import Enum

class SeatStatus(Enum):
    AVAILABLE = 1
    BOOKED = 2

class SeatType(Enum):
    ECONOMY = 1
    PREMIUM_ECONOMY = 2
    BUSINESS = 3
    FIRST_CLASS = 4

class Seat:

    def __init__(self, number,  type):
        self.number = number
        self.status = SeatStatus.AVAILABLE
        self.type = type

    def get_seat_no(self):
        return self.seat_no

    def book_seat(self):
        self.status = SeatStatus.BOOKED

    def cancel_seat(self):
        self.status = SeatStatus.AVAILABLE

    def get_seat_type(self):
        return self.type

    def get_seat_status(self):
        return self.status
