from abc import ABC

class Payment_Method(ABC):
    def process_payment(self, amount):
        pass