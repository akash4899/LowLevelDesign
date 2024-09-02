from state import State


class HasCardState(State):

    def insert_card(self, card, password):
        print("The machine already has a card inserted!")

    def withdraw_cash(self, amount):
        flag = self.atm_machine.current_card.user_account.withdraw_cash(amount)
        if flag == True:
            self.atm_machine.dispense_cash(amount)
        self.atm_machine.change_state(self.atm_machine.idle_state)

    def check_balance(self, card):
        self.atm_machine.change_state(self.atm_machine.idle_state)
        return card.user_account.check_balance()

