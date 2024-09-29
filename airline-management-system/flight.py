
class Flight:
    def __init__(self, id, src, destn, date, departure_time, arrival_time):
        self.src = src
        self.id = id
        self.destn = destn
        self.date = date
        self.seats = []
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    def get_src(self):
        return self.src

    def get_destn(self):
        return self.destn

    def get_date(self):
        return self.date

    def get_seats(self):
        return self.seats

    def update_date(self, date):
        self.date = date

    def get_departure_time(self):
        return self.departure_time

    def get_arrival_time(self):
        return self.arrival_time

    def update_destn(self, destn):
        self.destn = destn

    def update_src(self, src):
        self.src = src