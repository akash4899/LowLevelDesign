import uuid

from account import Account
from threading import Lock
class AccountManager:
    def __init__(self):
        self.accounts = {}
        self.lock = Lock()

    def add_account(self, currency, balance):
        account_number = self.generate_account_number()
        account = Account(account_number, currency, balance)
        self.accounts[account_number] = account
        return account

    def generate_account_number(self):
        return f"ACC{uuid.uuid4().hex[:8].upper()}"

    def remove_account(self, account_number):
        with self.lock:
            account = self.accounts.get(account_number)
            if account:
                self.accounts.pop(account_number)

