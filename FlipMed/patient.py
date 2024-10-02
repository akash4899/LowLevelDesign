class Patient:
    def __init__(self, name):
        self.name = name
        self.appointments = []

    def add_appointment(self, appointment):
        self.appointments.append(appointment)