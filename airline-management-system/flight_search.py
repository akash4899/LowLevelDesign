# from flight import Flight
class FlightSearch:
    def __init__(self, flights):
        self.flights = flights

    def search(self, src, destn, date):
        flights = []
        for flight in self.flights:
            if (src.lower() == flight.get_src().lower()
                    and flight.get_destn().lower() == destn.lower()
                    and flight.get_date() == date):
                flights.append(flight)

        return flights

