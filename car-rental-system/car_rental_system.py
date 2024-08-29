from user import User
from car import Car
from payment_processor import PaymentProcessor
from credit_card_payment_processor import CreditCardPaymentProcessor
from reservation import Reservation
from threading import Lock


class CarRentalSystem:
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls.users = []
                cls.cars = []
                cls.reservations = []
                cls.payment_processor = CreditCardPaymentProcessor()

        return cls._instance

    @classmethod
    def get_instance(cls):
        return cls()

    def add_car(self, car):
        self.cars.append(car)

    def remove_car(self, car):
        self.cars.remove(car)

    def search_cars(self, company, start_date, end_date):
        available_cars = []
        for car in self.cars:
            if  car.company.lower() == company.lower() and car.available:
                if self.is_car_available(car, start_date, end_date):
                    available_cars.append(car)
        return available_cars

    def is_car_available(self, car, start_date, end_date):
        for reservation in self.reservations:
            if reservation.get_car() == car:
                if start_date < reservation.get_end_date() and end_date > reservation.get_start_date():
                    return False
        return True

    def make_reservation(self, customer, car, start_date, end_date):
        if self.is_car_available(car, start_date, end_date):
            reservation = Reservation( customer, car, start_date, end_date)
            self.reservations.append(reservation)
            car.set_available(False)
            return reservation
        return None

    def cancel_reservation(self, reservation_id):
        reservation = self.reservations.remove(reservation_id)
        if reservation is not None:
            reservation.get_car().set_available(True)

    def process_payment(self, reservation):
        return self.payment_processor.process_payment(reservation.get_total_price())


