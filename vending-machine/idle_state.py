from state import State
from product import Product

class IdleState(State):
    def __init__(self, vending_machine):
        super().__init__(vending_machine)

    def select_product(self, product: Product):
        if self.vending_machine.inventory.is_available(product):
            self.vending_machine.selected_product = product
            self.vending_machine.set_state(self.vending_machine.ready_state)
            print(self.vending_machine.current_state)
            print(f"You selected: {product.name}")
        else:
            print("Product not available! Try something else.")

    def insert_coin(self, coin):
        print("Please Select a product first!")

    def insert_note(self, note):
        print("Please Select a product first!")

    def dispense_product(self):
        print("Please Select a product first!")

    def return_change(self):
        print("Please Select a product first!")

