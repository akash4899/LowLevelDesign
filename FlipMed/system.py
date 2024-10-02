import uuid
from threading import Lock
from doctor import Doctor
from patient import Patient
from slot import Slot, AvailabilityStatus
import datetime
from booking import Booking

class System:
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls.doctors = {}
                cls.patients = {}
                cls.bookings = {}
            return cls._instance

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls()
        return cls._instance

    def register_doctor(self, name, speciality):
        if self.doctors.get(name) is None:
            doctor = Doctor(name, speciality)
            self.doctors[name] = doctor
            return doctor
        print(f"Doctor {name} already exists")

    def register_patient(self, name):
        if self.patients.get(name) is None:
            patient = Patient(name)
            self.patients[name] = patient
            return patient
        print(f"Patient {name} already exists.")

    def add_doctor_slots(self, doctor, starting_time, ending_time):
        starting_time = datetime.datetime.strptime(starting_time, "%H%M")
        ending_time = datetime.datetime.strptime(ending_time, "%H%M")
        if ending_time<=starting_time:
            print("Ending time should be longer than starting time.")
        elif (ending_time-starting_time).seconds/60 == 30:
            new_slot = Slot(starting_time, ending_time)
            doctor.add_slot(new_slot)
            print("Done Doc.")
        else:
            print("Slot should be of half an hour.")

    def show_availability_by_speciality(self, speciality):
        for doctor in self.doctors.values():
            if doctor.speciality == speciality:
                print(f"{doctor.name}")
                for slot in doctor.slots:
                    if slot.availability_status == AvailabilityStatus.AVAILABLE:
                        print(f"{slot.starting_time}-{slot.ending_time}")


    def book_appointment(self, patient, doctor, starting_time):
        starting_time = datetime.datetime.strptime(starting_time, "%H%M")
        patient = self.patients.get(patient)
        doctor = self.doctors.get(doctor)
        if patient and doctor:
            for slot in doctor.slots:
                # print("*************************************************************************")
                # print(slot.starting_time)
                if slot.starting_time == starting_time:
                    if slot.availability_status == AvailabilityStatus.AVAILABLE:
                        booking_id = self.get_booking_id()
                        booking = Booking(booking_id, doctor, patient, slot)
                        self.bookings[booking_id] = booking
                        slot.availability_status = AvailabilityStatus.BOOKED
                        print(f"Slot Booked.{booking_id}")
                        print(booking)
                        return booking
                    else:
                        slot.waitlist.append(patient)
        print("SLot booking failed.")

    def cancel_booking(self, booking_id):
        booking = self.bookings.get(booking_id)
        if booking:
            booking.cancel_booking()
            print(f"Booking {booking_id} cancelled.")
            if len(booking.slot.waitlist)>0:
                patient = booking.slot.waitlist[0]
                doctor = booking.doctor
                self.book_appointment(patient, doctor, booking.slot.starting_time)
                booking.slot.pop(0)

    def get_booking_id(self):
        return f"BOOK{uuid.uuid4().hex[:8].upper()}"