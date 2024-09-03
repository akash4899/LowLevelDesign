from hotel_management_system import HotelManagementSystem
from hotel_management_system import HotelManagementSystem
from guest import Guest
from room import Room
from single_room import SingleRoom
from credit_card_payment_processor import CreditCardPaymentProcessor
from datetime import date

class Demo:
    @staticmethod
    def run():
        hotel_management_system = HotelManagementSystem()

        # Create guests
        guest1 = Guest( "John Doe", "john@example.com", "1234567890")
        guest2 = Guest( "Jane Smith", "jane@example.com", "9876543210")
        hotel_management_system.add_guest(guest1)
        hotel_management_system.add_guest(guest2)

        # Create rooms
        room1 = SingleRoom("R001")
        room2 = SingleRoom("R002")
        hotel_management_system.add_room(room1)
        hotel_management_system.add_room(room2)

        # Book a room
        check_in_date = date.today()
        check_out_date = check_in_date.replace(day=check_in_date.day + 3)
        reservation1 = hotel_management_system.book_room(guest1, room1, check_in_date, check_out_date)
        if reservation1:
            print(f"Reservation created: {reservation1.id}")
        else:
            print("Room not available for booking.")

        # Check-in
        hotel_management_system.check_in(reservation1.id)
        print(f"Checked in: {reservation1.id}")

        # Check-out and process payment
        payment = CreditCardPaymentProcessor()
        hotel_management_system.check_out(reservation1.id, payment)
        print(f"Checked out: {reservation1.id}")

        # Cancel a reservation
        hotel_management_system.cancel_reservation(reservation1.id)
        print(f"Reservation cancelled: {reservation1.id}")

if __name__ == "__main__":
    Demo.run()