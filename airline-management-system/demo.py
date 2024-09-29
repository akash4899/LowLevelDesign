from system import System
from passenger import Passenger
from datetime import datetime, timedelta, date
from flight import Flight
from aircraft import Aircraft
from typing import List
from seat import Seat, SeatStatus, SeatType


class Demo:
    @staticmethod
    def run():
        airline_management_system = System()

        # Create users
        passenger1 = Passenger("U001", "John Doe", "john@example.com", "1234567890")

        # Create flights
        departure_time1 = datetime.now() + timedelta(days=1)
        arrival_time1 = departure_time1 + timedelta(hours=2)
        date1 = date.today() + timedelta(days=2)
        flight1 = Flight("F001", "New York", "London", date1, departure_time1, arrival_time1)

        departure_time2 = datetime.now() + timedelta(days=3)
        arrival_time2 = departure_time2 + timedelta(hours=5)
        flight2 = Flight("F002", "Paris", "Tokyo", date1, departure_time2, arrival_time2)

        airline_management_system.add_flight(flight1)
        airline_management_system.add_flight(flight2)

        # Create aircrafts
        aircraft1 = Aircraft("A001", "Boeing 747", 300)
        aircraft2 = Aircraft("A002", "Airbus A380", 500)
        airline_management_system.add_aircraft(aircraft1)
        airline_management_system.add_aircraft(aircraft2)

        # Search flights
        search_date = datetime.now().date() + timedelta(days=1)
        search_results: List[Flight] = airline_management_system.search_flights("New York", "London", search_date)
        print("Search Results:")
        for flight in search_results:
            print(f"Flight: {flight.flight_number} - {flight.source} to {flight.destination}")

        seat = Seat("25A", SeatType.ECONOMY)

        # Book a flight
        booking1 = airline_management_system.book_flight(flight1, passenger1, seat, 100)
        if booking1:
            #print(booking1)
            print(f"Booking successful. Booking ID: {booking1.id}")
        else:
            print("Booking failed.")

        # Cancel a booking
        airline_management_system.cancel_booking(booking1.id)
        print("Booking cancelled.")


if __name__ == '__main__':
    Demo.run()
