from car_rental_system import CarRentalSystem
from car import Car
from payment_processor import PaymentProcessor
from user import User
from datetime import date, timedelta

class CarRentalSystemDemo:
    @staticmethod
    def run():
            rental_system = CarRentalSystem.get_instance()

            # Add cars to the rental system
            rental_system.add_car(Car("Hyundai",  2022, "ABC123", 50.0, 10000))
            rental_system.add_car(Car("Suzuki",  2021, "XYZ789", 45.0, 5000))
            rental_system.add_car(Car("Ford", 2023, "DEF456", 80.0, 4000))

            # Create customers
            customer1 = User("John Doe", "john@example.com", "DL1234")
            customer2 = User("Jane Smith", "jane@example.com", "DL5678")

            # Make reservations
            start_date = date.today()
            end_date = start_date + timedelta(days=3)
            available_cars = rental_system.search_cars("Hyundai", start_date, end_date)

            if available_cars:
                selected_car = available_cars[0]
                # print(selected_car.company)
                reservation = rental_system.make_reservation(customer1, selected_car, start_date, end_date)
                if reservation is not None:
                    payment_success = rental_system.process_payment(reservation)
                    if payment_success:
                        print(f"Reservation successful. Reservation ID: {reservation.get_reservation_id()}")
                    else:
                        print("Payment failed. Reservation canceled.")
                        rental_system.cancel_reservation(reservation.get_reservation_id())
                else:
                    print("Selected car is not available for the given dates.")
            else:
                print("No available cars found for the given criteria.")

if __name__ == "__main__":
    CarRentalSystemDemo.run()

