from datetime import datetime

class UserAccount:
    def __init__(self, name, cards=None):
        self.name = name
        self.cards = cards
        self.balance = 5000
        self.created_at = datetime.now()
        self.last_transaction = self.created_at

    def withdraw_cash(self, cash):
        if self.balance < cash:
            print(f"Your balance is {self.balance}, you cannot withdraw more than this amount.")
            return False
        else:
            self.balance = self.balance-cash
            return True

    def check_balance(self):
        # print(self.balance)
        return self.balance

    def add_card(self, card):
        self.cards.append(card)

