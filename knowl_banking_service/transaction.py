from threading import Lock
class Transaction:
    def __init__(self, time, account, amount, amount_type, transaction_type):
        self.time = time
        self.account = account
        self.amount = amount
        self.amount_type = amount_type
        self.transaction_type = transaction_type
        self.status = "FAILED"
        self.lock = Lock()

    def execute(self):
        with self.lock:
            if self.amount_type == 'CREDIT':
                # print(self.amount_type)
                # print(self.account.deposit_amount(self.amount))
                if self.account.deposit_amount(self.amount) == 'SUCCESS':
                    self.status = 'SUCCESS'
                return
            else:
                if self.account.withdraw_amount(self.amount) == "SUCCESS":
                    self.status = 'SUCCESS'
                return
