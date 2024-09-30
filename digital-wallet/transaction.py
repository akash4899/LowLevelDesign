

class Transaction:
    def __init__(self, id, src, dest, amount, currency, timestamp):
        self.id = id
        self.src = src
        self.dest = dest
        self.amount = amount
        self.currency = currency
        self.timestamp = timestamp

    def get_src(self):
        return self.src

    def get_dest(self):
        return self.dest

    def get_amount(self):
        return self.amount

    def get_time(self):
        return self.timestamp