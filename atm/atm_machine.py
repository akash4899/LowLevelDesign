from state import State
from idle_state import IdleState
from user_account import UserAccount
from has_card_state import HasCardState
from threading import Lock

class ATMMachine:
    _lock = Lock()
    _instance = None

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls.idle_state = IdleState(cls._instance)
                cls.has_card_state = HasCardState(cls._instance)
                cls.curr_state  = cls.idle_state
                cls.user_accounts = []
                cls.cards = []
                cls.current_card = None
        return cls._instance

    @classmethod
    def get_instance(cls):
        return cls()

    def insert_card(self, card, password):
        self.curr_state.insert_card(card, password)
        #print(self.curr_state)

    def withdraw_amount(self, amount):
        self.curr_state.withdraw_cash(amount)

    def check_balance(self, card):
        print(self.curr_state.check_balance(card))

    def change_state(self, state):
        self.curr_state = state

    def dispense_cash(self, amount):
        print(f"Dispensing cash worth {amount}")
