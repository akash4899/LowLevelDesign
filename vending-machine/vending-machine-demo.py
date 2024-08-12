from vending_machine import VendingMachine
from product import Product
from coin import Coin
from note import Note

class VendingMachineDemo:
    @staticmethod
    def run():
        vending_machine = VendingMachine.get_instance()

        coke = Product('Coke',  25)
        pepsi = Product('Pepsi',  20)
        water = Product('Water',  10)

        vending_machine.inventory.add_product(coke, 5)
        vending_machine.inventory.add_product(pepsi, 3)
        vending_machine.inventory.add_product(water, 2)

        vending_machine.select_product(coke)

        vending_machine.insert_coin(Coin(1))
        vending_machine.insert_coin(Coin(2))
        vending_machine.insert_coin(Coin(2))

        vending_machine.insert_note(Note(10))
        vending_machine.insert_note(Note(10))


        vending_machine.dispense_product()


        vending_machine.return_change()

if __name__ == "__main__":
    VendingMachineDemo.run()
