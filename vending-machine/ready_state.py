from state import State
from product import Product
from coin import Coin
from note import Note

class ReadyState(State):
    def __init__(self, vending_machine):
        super().__init__(vending_machine)

    def select_product(self, product: Product):
        print("You have already selected a product! Please do the payment")

    def insert_coin(self, coin):
        self.vending_machine.add_coin(coin)
        print(f"Coin inserted: {coin.value}")
        self.check_payment_status()


    def insert_note(self, note):
        self.vending_machine.add_coin(note)
        print(f"Coin inserted: {note.value}")
        self.check_payment_status()

    def dispense_product(self):
        print("Please insert money first!")

    def return_change(self):
        change = self.vending_machine.total_payment - self.vending_machine.selected_product.price
        if change>0:
            print(f"You get back {change} Rs")
            self.vending_machine.reset_payment()
        else:
            print("No change to return.")
        self.vending_machine.set_state(self.vending_machine.idle_state)

    def check_payment_status(self):
        if self.vending_machine.total_payment >= self.vending_machine.selected_product.price:
            self.vending_machine.set_state(self.vending_machine.dispense_state)

