class Centre:
    def __init__(self, centre_id, centre_name):
        self.centre_id = centre_id
        self.centre_name = centre_name
        self.vaccine_inventory = {}
        self.bookings = 0
        self.users = []

    def add_inventory(self, vaccine_type, quantity):
        if self.vaccine_inventory.get(vaccine_type):
            self.vaccine_inventory[vaccine_type] += quantity
        else:
            self.vaccine_inventory[vaccine_type] = quantity

    def get_vaccine_quantity(self, vaccine_type):
        vaccines = self.vaccine_inventory.get(vaccine_type)
        if vaccines:
            return vaccines
        return 0

    def get_number_of_bookings(self):
        return self.bookings

    def book_slot(self, user, vaccine_type):
        if self.vaccine_inventory.get(vaccine_type):
            self.bookings += 1
            self.users.append(user)
            self.vaccine_inventory[vaccine_type] -= 1
            return 1
        return 0