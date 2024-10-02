from system import System
from vaccine_type import VaccineType

class Demo:
    @staticmethod
    def run():
        system = System.get_instance()

        user1 = system.register_user('User1', VaccineType.COVAX, 'M')
        user2 = system.register_user('User2', VaccineType.COVISHIELD, 'F')

        centre1 = system.register_centre('Centre1')
        centre2 = system.register_centre('Centre2')

        system.add_inventory_to_centre(centre1.centre_id, VaccineType.COVISHIELD, 5)
        system.add_inventory_to_centre(centre1.centre_id, VaccineType.COVAX, 10)

        system.add_inventory_to_centre(centre2.centre_id, VaccineType.COVAX, 10)

        centres_list  = system.get_centres(user1)

        for centre in centres_list:
            print(f"{centre[2]} {user1.preferred_vaccine_type}-{centre[0]}")

        book_slot = system.book_slot(user2, centre2.centre_id)
        print(book_slot)

        book_slot = system.book_slot(user1, centre1.centre_id)
        print(book_slot)

        system.get_stats()

if __name__ == "__main__":
    Demo.run()