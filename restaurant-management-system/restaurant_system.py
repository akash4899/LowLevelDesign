from threading import Lock
from menu import Menu
import uuid
from order import Order
from bill import Bill
from credit_card_payment import CreditCardPayment
from customer import Customer
from reservation import Reservation

class System:
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls.customers = {}
                cls.orders = {}
                cls.bills = {}
                cls.reservations = {}
                cls.menu = None
                cls.payments = {}
        return cls._instance


    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls()
        return cls._instance

    def add_menu(self, items):
        self.menu = Menu(items)

    def add_item_to_menu(self):
        pass

    def place_order(self, items):
        order_id = self.create_order_id()
        order = Order(order_id, items)
        self.orders[order_id] = order
        print(f"Order created with order_id: {order_id}")
        return order

    def pay_bill(self, bill):
        payment_id = self.create_payment_id()
        payment = CreditCardPayment(payment_id, bill)
        self.payments[payment_id] = payment
        payment.pay()

    def create_reservation(self, datetime, customer):
        reservation_id = self.create_reservation_id()

        self.reservations[reservation_id] = customer.make_reservation(reservation_id, datetime)

    def create_order_id(self):
        return f"ORD{uuid.uuid4().hex[:8].upper()}"

    def create_bill_id(self):
        return f"BILL{uuid.uuid4().hex[:8].upper()}"

    def create_payment_id(self):
        return f"BILL{uuid.uuid4().hex[:8].upper()}"

    def create_reservation_id(self):
        return f"RES{uuid.uuid4().hex[:8].upper()}"


