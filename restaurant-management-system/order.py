from enum import Enum
import uuid
from bill import Bill

class OrderStatus(Enum):
    PLACED='Placed'
    PREPARED='Prepared'
    Delivered='Delivered'


class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items
        self.bill = self.create_bill()
        self.order_status = OrderStatus.PLACED

    def create_bill(self):
        bill_id = self.create_bill_id()
        self.bill = Bill(bill_id, self)
        #print(f"")
        print(f"Bill created for  with bill id {self.bill.bill_id}")
        return self.bill

    def deliver_order(self):
        self.order_status = OrderStatus.Delivered
        print("Order Delivered.")

    def prepare_order(self):
        self.order_status = OrderStatus.PREPARED

    def create_bill_id(self):
        return f"BILL{uuid.uuid4().hex[:8].upper()}"
