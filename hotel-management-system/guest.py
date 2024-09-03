

class Guest:

    def __init__(self, name, email, phone_number):
        self.name = name
        self.id = id(self)
        self.email = email
        self.phone_number = phone_number


