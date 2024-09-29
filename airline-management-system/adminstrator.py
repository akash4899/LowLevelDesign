from person import Person

class Administrator(Person):
    def __init__(self, id, name, contact):
        self.id = id
        self.name = name
        self.contact = contact