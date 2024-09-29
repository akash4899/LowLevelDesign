from enum import Enum

class PaymentStatus(Enum):
    COMPLETED = 'Completed'
    PENDING = 'Pending'

class Payment:

    def __init__(self, id, amount, payment_status):
        self.id = id
        self.amount = amount
        self.payment_status = payment_status

    def get_amount(self):
        return self.amount

    def get_payment_status(self):
        return self.payment_status

    def update_payment_status(self, payment_status):
        self.payment_status = payment_status

    def process_payment(self):
        print("payment done.")

