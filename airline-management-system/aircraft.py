

class Aircraft:
    def __init__(self, tail_number, model, total_seats):
        self.tail_number = tail_number
        self.model = model
        self.total_seats = total_seats

    def get_tail_number(self):
        return self.tail_number

    def get_model(self):
        return self.model

    def get_total_seats(self):
        return self.total_seats
