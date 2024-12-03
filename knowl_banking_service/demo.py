from bank_account import BankAccount
from transaction import Transaction
from banking_system import BankingSystem


class Demo:
    @staticmethod
    def run():
        banking_system = BankingSystem.get_instance()

        banking_system.add_bank_account("Knowl1", 100)
        banking_system.add_bank_account("Knowl2", 100)
        # print(banking_system.withdraw_amount("Knowl1", 50, 'ATM'))
        # print(banking_system.deposit_amount("Knowl1", 200, "Instant"))
        print(banking_system.instant_transfer("Knowl1", "Knowl2", 50))


if __name__ == "__main__":
    Demo.run()