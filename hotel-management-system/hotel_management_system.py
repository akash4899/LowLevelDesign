from threading import Lock
from guest import Guest
from room import Room
from reservation import Reservation
from typing import Dict
from room_status import RoomStatus
import uuid
from reservation_status import ReservationStatus
class HotelManagementSystem:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.guests: Dict[str, Guest] = {}
            cls._instance.rooms: Dict[str, Room] = {}
            cls._instance.reservations: Dict[str, Reservation] = {}
            cls._instance.lock = Lock()
        return cls._instance

    def add_guest(self, guest: Guest):
        self.guests[guest.id] = guest

    def get_guest(self, guest_id: str):
        return self.guests.get(guest_id)

    def add_room(self, room: Room):
        self.rooms[room.room_number] = room

    def get_room(self, room_number: str):
        return self.rooms.get(room_number)

    def book_room(self, guest, room, check_in_date, check_out_date):
        with self.lock:
            if room.status == RoomStatus.AVAILABLE:
                room.book()
                reservation_id = self.generate_reservation_id()
                reservation = Reservation(reservation_id, guest, room, check_in_date, check_out_date)
                self.reservations[reservation_id] = reservation
                return reservation
            return None

    def check_in(self, reservation_id: str):
        with self.lock:
            reservation = self.reservations.get(reservation_id)
            if reservation and reservation.status == ReservationStatus.CONFIRMED:
                reservation.room.check_in()
            else:
                raise ValueError("Invalid reservation or reservation not confirmed.")

    def check_out(self, reservation_id: str, payment):
        with self.lock:
            reservation = self.reservations.get(reservation_id)
            if reservation and reservation.status == ReservationStatus.CONFIRMED:
                room = reservation.room
                amount = room.price * (reservation.check_out_date - reservation.check_in_date).days
                if payment.process_payment(amount):
                    room.check_out()
                    del self.reservations[reservation_id]
                else:
                    raise ValueError("Payment failed.")
            else:
                raise ValueError("Invalid reservation or reservation not confirmed.")

    def cancel_reservation(self, reservation_id: str):
        with self.lock:
            reservation = self.reservations.get(reservation_id)
            if reservation:
                reservation.cancel()
                del self.reservations[reservation_id]

    def generate_reservation_id(self):
        return f"RES{uuid.uuid4().hex[:8].upper()}"