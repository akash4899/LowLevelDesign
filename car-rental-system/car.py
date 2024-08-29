class Car:
    def __init__(self, company, model, year, license_plate, per_day_price):
        self.company = company
        self.model = model
        self.year = year
        self.license_plate = license_plate
        self.per_day_price = per_day_price
        self.available = True

    def book_car(self):
        self.is_available = False

    def get_rental_price_per_day(self):
        return self.per_day_price

    def get_license_plate(self):
        return self.license_plate


    def get_model(self):
        return self.model

    def is_available(self):
        return self.available

    def set_available(self, available):
        self.available = available