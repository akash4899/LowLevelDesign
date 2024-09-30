from threading import Lock

class Account:
    def __init__(self, account_number, currency, balance):
        self.account_number = account_number
        self.currency = currency
        self.balance = balance
        self.transaction_history = []
        self._lock = Lock()


    def deposit(self, money):
        with self._lock:
            self.balance += money

    def withdraw(self, money):
        with self._lock:
            if self.balance >= money:
                self.balance -= money
            else:
                print("Insufficient Balance.")

    def add_transaction(self, transaction):
        self.transaction_history.append(transaction)


