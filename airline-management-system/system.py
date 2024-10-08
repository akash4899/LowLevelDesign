from threading import Lock
from passenger import Passenger
from bookingmanager import BookingManager
from payment_processor import PaymentProcessor
from flight_search import FlightSearch

class System:
    def __init__(self):
        self.flights = []
        self.aircrafts = []
        self.flight_search = FlightSearch(self.flights)
        self.booking_manager = BookingManager()
        self.payment_processor = PaymentProcessor()

    def add_flight(self, flight):
        self.flights.append(flight)

    def add_aircraft(self, aircraft):
        self.aircrafts.append(aircraft)

    def search_flights(self, source, destination, date):
        return self.flight_search.search(source, destination, date)

    def book_flight(self, flight, passenger, seat, price):
        return self.booking_manager.create_booking(flight, passenger, seat, price)

    def cancel_booking(self, booking_number):
        self.booking_manager.cancel_booking(booking_number)

    def process_payment(self, payment):
        self.payment_processor.process_payment(payment)
