

class Reservation:
    def __init__(self, user, car, start_date, end_date):
        self.reservation_id = id(self)
        self.user = user
        self.car = car
        self.start_date = start_date
        self.end_date = end_date
        self.total_price = self.calculate_price()


    def calculate_price(self):
        return ((self.end_date - self.start_date).days + 1)*self.car.per_day_price

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def get_car(self):
        return self.car

    def get_total_price(self):
        return self.total_price

    def get_reservation_id(self):
        return self.reservation_id
