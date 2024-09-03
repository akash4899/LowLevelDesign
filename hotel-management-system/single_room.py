from room import Room
from room_status import RoomStatus

from threading import Lock

class SingleRoom:
    def __init__(self, room_number):
        self.room_number = room_number
        self.status = RoomStatus.AVAILABLE
        self.price = 500
        self.lock = Lock()

    def book(self):
        with self.lock:
            if self.status == RoomStatus.AVAILABLE:
                self.status = RoomStatus.BOOKED
            else:
                raise ValueError("Room is not available for booking.")

    def check_in(self):
        with self.lock:
            if self.status == RoomStatus.BOOKED:
                self.status = RoomStatus.OCCUPIED
            else:
                raise ValueError("Room is not  booked.")

    def check_out(self):
        with self.lock:
            if self.status == RoomStatus.OCCUPIED:
                self.status = RoomStatus.AVAILABLE
            else:
                raise ValueError("Room is not occupied.")

    def get_room_number(self):
        return self.room_number

    def get_price(self):
        return self.price

    def get_room_status(self):
        return self.status
