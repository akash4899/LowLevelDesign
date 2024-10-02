from enum import Enum

class BookingStatus(Enum):
    BOOKED = 'Booked'
    Canceled = 'Canceled'

class Booking:
    def __init__(self, id, doctor, patient, slot):
        self.id = id
        self.doctor = doctor
        self.patient = patient
        self.slot = slot
        self.status = BookingStatus.BOOKED

    def cancel_booking(self):
        self.slot.cancel_slot()
        self.status = BookingStatus.Canceled