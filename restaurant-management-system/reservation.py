from enum import Enum

class ReservationStatus(Enum):
    BOOKED='Booked'
    CANCELED='Canceled'
    COMPLETED='Completed'
class Reservation:
    def __init__(self, reservation_id, datetime):
        self.reservation_id = reservation_id
        self.datetime = datetime
        self.reservation_status = ReservationStatus.BOOKED
        print("reservation created.")

    def cancel(self):
        self.reservation_status = ReservationStatus.CANCELED
        print("Canceled Reservation")
