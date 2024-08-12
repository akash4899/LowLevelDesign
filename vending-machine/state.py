from abc import ABC, abstractmethod

class State(ABC):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    @abstractmethod
    def select_product(self, product):
        pass

    @abstractmethod
    def insert_coin(self, coin):
        pass

    @abstractmethod
    def insert_note(self, note):
        pass

    @abstractmethod
    def dispense_product(self):
        pass

