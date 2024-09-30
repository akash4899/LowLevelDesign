from payment_method import Payment_Method

class BankAccount(Payment_Method):
    def __init__(self, bank_name, account_number, balance):
        self.bank_name = bank_name
        self.account_number = account_number
        self.balance = balance

    def process_payment(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return 1
        else:
            return 0

