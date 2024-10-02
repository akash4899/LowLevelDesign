from enum import Enum

class AvailabilityStatus(Enum):
    AVAILABLE = 'Available'
    BOOKED = 'Booked'
class Slot:
    def __init__(self, starting_time, ending_time):
        self.starting_time = starting_time
        self.ending_time = ending_time
        self.availability_status = AvailabilityStatus.AVAILABLE
        self.waitlist = []

    def book_slot(self):
        if self.availability_status == AvailabilityStatus.AVAILABLE:
            self.availability_status = AvailabilityStatus.BOOKED
            print("Slot Booked")
        print("Slot already booked.")

    def cancel_slot(self):
        if self.availability_status == AvailabilityStatus.BOOKED:
            self.availability_status = AvailabilityStatus.AVAILABLE
            print("Slot Canceled.")
        else:
            print("Slot wasnt booked.")

    def add_waitlist(self, patient):
        self.waitlist.append(patient)
