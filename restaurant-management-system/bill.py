
from enum import Enum

class PaymentStatus(Enum):
    UNPAID='Unpid'
    PAID='Paid'

class Bill:

    def __init__(self, bill_id, order):
        self.bill_id = bill_id
        self.order = order
        self.total_cost = self.calculate_price()
        self.payment_status = PaymentStatus.UNPAID

    def calculate_price(self):
        total_cost = 0
        for item in self.order.items:
            total_cost += item.price

        return total_cost

    def get_total_cost(self):
        return self.total_cost

    def get_list_of_items(self):
        return self.items
