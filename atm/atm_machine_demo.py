from atm_machine import ATMMachine
from card import Card
from user import  User
from user_account import UserAccount


class Demo:
    @staticmethod
    def run():
        atm_machine = ATMMachine.get_instance()

        user_account1 = UserAccount("John")

        card1 = Card('12345', '123', user_account1, '0000')

        #print(card1.user_account.name)

        atm_machine.insert_card(card1, '0000')
        atm_machine.check_balance(card1)
        atm_machine.insert_card(card1, '0000')
        atm_machine.withdraw_amount(2000)


if __name__ == '__main__':
    Demo.run()
