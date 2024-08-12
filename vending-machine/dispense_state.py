from state import State
from product import Product
from coin import Coin
from note import Note

class DispenseState(State):
    def __init__(self, vending_machine):
        super().__init__(vending_machine)

    def select_product(self, product: Product):
        print("You have already selected a product! Please collect the product.")

    def insert_coin(self, coin):
        print("Payment already done. please collect the product.")


    def insert_note(self, note):
        print("Payment already done. please collect the product.")

    def dispense_product(self):
        self.vending_machine.set_state(self.vending_machine.ready_state)
        product = self.vending_machine.selected_product
        self.vending_machine.inventory.update_quantity(product, self.vending_machine.inventory.get_quantity(product) - 1)
        print(f"Product dispensed: {product.name}")
        self.vending_machine.set_state(self.vending_machine.return_change_state)


    def return_change(self):
        print("Please collect the dispensed product first.")



