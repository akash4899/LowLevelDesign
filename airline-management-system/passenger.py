from person import Person
class Passenger(Person):
    def __init__(self, id, name, contact, baggage_info):
        super().__init__(id, name, contact)
        self.baggage_info = baggage_info

    def get_baggage_info(self):
        return self.baggage_info