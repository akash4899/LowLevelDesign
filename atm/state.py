from abc import ABC, abstractmethod

class State(ABC):

    def __init__(self, atm_machine):
        self.atm_machine = atm_machine
    @abstractmethod
    def insert_card(self, card):
        pass

    @abstractmethod
    def withdraw_cash(self, amount):
        pass

    @abstractmethod
    def check_balance(self, user_account):
        pass
