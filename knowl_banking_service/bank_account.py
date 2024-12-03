
class BankAccount:
    def __init__(self, id, balance):
        self.balance = balance
        self.id = id

    def get_balance(self):
        return self.balance

    def deposit_amount(self, amount):
        self.balance += amount
        return "SUCCESS"

    def withdraw_amount(self, amount):
        if amount > self.balance:
            return "FAILED"

        self.balance -= amount

        return "SUCCESS"
