import datetime
import uuid
from threading import Lock
from user_manager import UserManager
from account_manager import AccountManager
from transaction import Transaction
from currency_convertor import CurrencyConverter
class DigitalWallet:
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls.user_manager = UserManager()
                cls.account_manager = AccountManager()
                cls.transactions = {}
                cls.lock = Lock()
        return cls._instance

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls()
        return cls._instance

    def add_user(self, name, contact_number, email, password):
        return self.user_manager.add_user(name, contact_number, email, password)

    def remove_user(self, user_id):
        self.user_manager.remove_user(user_id)

    def add_account(self, currency, balance):
        return self.account_manager.add_account(currency, balance)

    def remove_account(self, account_id):
        self.account_manager.remove_account(account_id)

    def transfer_funds(self, source_account, destination_account, amount, currency):
        if source_account.currency != currency:
            amount = CurrencyConverter.convert_currency(amount, currency, source_account.currency)
        source_account.withdraw(amount)

        if destination_account.currency != currency:
            amount = CurrencyConverter.convert_currency(amount, currency, destination_account.currency)
        destination_account.deposit(amount)

        transaction_id = self._generate_transaction_id()
        transaction = Transaction(transaction_id, source_account, destination_account, amount, currency, datetime.datetime.now())
        source_account.add_transaction(transaction)
        destination_account.add_transaction(transaction)

    def get_transaction_history(self, account):
        return account.transaction_history

    def _generate_transaction_id(self):
        return "TXN" + str(uuid.uuid4()).replace('-', '').upper()[:8]
