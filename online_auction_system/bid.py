import datetime


class Bid:
    def __init__(self, id, bidder, amount):
        self.id = id
        self.timestamp = datetime.datetime.now()
        self.amount = amount
        self.bidder = bidder
