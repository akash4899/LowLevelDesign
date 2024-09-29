from threading import Lock
from uuid import uuid4
from booking import Booking

class BookingManager:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.bookings = {}
        self.booking_counter = 0

    def create_booking(self, flight, passenger, seat, price):
        booking_id = self._generate_booking_id()
        #print("here")
        with self._lock:
            #print(booking_id)
            self.bookings[booking_id] = Booking(booking_id, flight, seat, passenger, price)
        return self.bookings[booking_id]

    def _generate_booking_id(self):
        return f"BOOK{uuid4().hex[:8].upper()}"

    def cancel_booking(self, booking_id):
        with self._lock:
            booking = self.bookings.get(booking_id)
            if booking:
                booking.cancel()




