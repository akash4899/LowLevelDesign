from state import State
from card import Card
class IdleState(State):

    def insert_card(self, card, password):
        self.atm_machine.current_card = card
        if card.password != password:
            print("Your password is incorrect! Insert card again and give correct password.")
            return
        self.atm_machine.change_state(self.atm_machine.has_card_state)

    def withdraw_cash(self, amount):
        print("Insert card first.")

    def check_balance(self, user_account):
        print("Insert card first.")
