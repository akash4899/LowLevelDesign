from abc import ABC

class Payment(ABC):
    def __init__(self, payment_id, bill):
        self.payment_id = payment_id
        self.bill = bill

    def pay(self):
        pass
