from doctor import Doctor, Speciality
from patient import Patient
from booking import Booking
from slot import Slot
from system import System

class Demo:
    @staticmethod
    def run():
        system = System()

        doctor1 = system.register_doctor("Curious", Speciality.CARDIOLOGIST)
        system.add_doctor_slots(doctor1, "930", "1030")
        system.add_doctor_slots(doctor1, "930", "1000")
        system.add_doctor_slots(doctor1, "1230", "1300")
        system.add_doctor_slots(doctor1, "1600", "1630")

        system.show_availability_by_speciality(Speciality.CARDIOLOGIST)

        patientA = system.register_patient("PatientA")
        booking = system.book_appointment("PatientA", "Curious", "1230")

        system.show_availability_by_speciality(Speciality.CARDIOLOGIST)
        print(f"*******************************{booking.id}******************")
        system.cancel_booking(booking.id)

        system.show_availability_by_speciality(Speciality.CARDIOLOGIST)


if __name__ == "__main__":
    Demo.run()


