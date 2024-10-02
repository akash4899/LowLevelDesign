from user import User
from restaurant import Restaurant
from review import Review
from food_item import FoodItem
from system import System


class Demo:
    @staticmethod
    def run():
        system = System()

        user1 = system.register_user("Pralove", "M", "phoneNumber-1", "HSR")
        user2 = system.register_user("Nitesh", "M", "phoneNumber-2", "BTM")
        user3 = system.register_user("Vatsal", "M", "phoneNumber-3", "BTM")

        system.login_user("phoneNumber-1")
        pin_codes_r1 = ["BTM", "HSR"]
        r1 = system.register_restaurant("Food Court-1", pin_codes_r1, "NI Thali", 100, 5)
        pin_codes_r2 = ["BTM"]
        r2 = system.register_restaurant("Food Court-2", pin_codes_r2, "Burger", 120, 3)

        system.login_user("phoneNumber-2")
        pin_codes_r3 = ["HSR"]
        r3 = system.register_restaurant("Food Court-3", pin_codes_r3, "SI Thali", 150, 1)

        system.login_user("phoneNumber-3")
        system.show_restaurant("price")

        system.place_order(r1, 2)
        system.create_review(r2, 3, "good food")
        system.create_review(r1, 5, "Nice food")
        #
        system.show_restaurant("rating")
        #
        system.login_user("phoneNumber-1")
        system.update_quantity(r2, 5)


if __name__ == "__main__":
    Demo.run()

