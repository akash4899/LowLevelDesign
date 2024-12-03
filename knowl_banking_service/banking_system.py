from bank_account import BankAccount
from transaction import Transaction
from threading import Lock
from datetime import datetime
class BankingSystem:
    _instance = None
    _lock = Lock()


    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls.bank_accounts = {}
                cls.transactions = {}

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls()
        return cls._instance

    def add_bank_account(self, bank_account_id, balance):
        # bank_account_id = self.generate_bank_account_id()
        bank_account = BankAccount(bank_account_id, balance)
        self.bank_accounts[bank_account_id] = bank_account

    def withdraw_amount(self, bank_account_id, amount, transaction_type):
        bank_account = self.bank_accounts.get(bank_account_id)

        if bank_account is None:
            return "Bank Account doesnt exist."

        timestamp = datetime.now()
        # print(timestamp)
        transaction = Transaction(timestamp, bank_account, amount, "DEBIT", transaction_type)

        transaction.execute()
        # print(transaction.status)
        if transaction.status == 'SUCCESS':
            self.transactions[timestamp] = transaction
            return "Withdraw Success"
        return "Withdraw failed."


    def deposit_amount(self, bank_account_id, amount, transaction_type):
        bank_account = self.bank_accounts.get(bank_account_id)
        if bank_account is None:
            return "Account does not exist."
        timestamp = datetime.now()
        # print(timestamp)
        transaction = Transaction(timestamp, bank_account, amount, "CREDIT", transaction_type)

        transaction.execute()

        if transaction.status == 'SUCCESS':
            self.transactions[timestamp] = transaction
            return "Deposit Succeeded"
        return "Deposit failed."

    def get_transactions(self):

        for transaction in self.transactions.values():
            print(transaction.time, transaction.account, transaction.amount, transaction.amount_type, transaction.transaction_type)


    def instant_transfer(self, from_account_id, to_account_id, amount):
        from_account = self.bank_accounts.get(from_account_id)
        to_account = self.bank_accounts.get(to_account_id)

        if from_account is None:
            return "Sender account doesnt exist"
        if to_account is None:
            return "Receiver account doesnt exist"

        lock = Lock()
        with lock:
            if self.withdraw_amount(from_account_id, amount, "INSTANT") == "Withdraw failed":
                return "Transaction Failed."
            if self.deposit_amount(from_account_id, amount, "INSTANT") == "Deposit failed.":
                return "Transaction Failed."
            return "transaction succceeded."
        return "Transaaction Failed."

