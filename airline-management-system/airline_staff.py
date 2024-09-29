from person import Person

class AirlineStafee(Person):
    def __init__(self, id, name, contact, schedule):
        super().__init__(id, name, contact)
        self.schedule = schedule

    def get_schedule(self):
        return self.schedule