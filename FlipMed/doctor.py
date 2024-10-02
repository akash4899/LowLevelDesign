from slot import Slot
from enum import Enum

class Speciality(Enum):
    CARDIOLOGIST = 'cardiologist'
    GENERALPHYSICIAN = 'General physician'
    DERMATOLOGIST = 'Dermatologist'
    ORTHOPEDIC = 'Orthopedic'

class Doctor:
    def __init__(self, name, speciality):
        self.name = name
        self.speciality = speciality
        self.slots = []
        print(f"Welcome Doctor {self.name}")

    def get_name(self):
        return self.name

    def get_speciality(self):
        return self.speciality

    def add_slot(self, slot):
        self.slots.append(slot)
