
class Person:
    def __init__(self, id, name, contact):
        self.id = id
        self.name = name
        self.contact = contact

    def get_name(self):
        return self.name

    def get_contact(self):
        return self.contact