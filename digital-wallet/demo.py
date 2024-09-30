from decimal import Decimal
from user import User
from account import Account
from currency import Currency
from digital_wallet_system import DigitalWallet
from credit_card import CreditCard
from bank_account import BankAccount

class DigitalWalletDemo:
    @staticmethod
    def run():
        digital_wallet = DigitalWallet.get_instance()

        # Create users

        user1 = digital_wallet.add_user("John Doe", "7878781232", "john@example.com", "password123")
        user2 = digital_wallet.add_user("Jane Smith", "7676292876","jane@example.com", "password456")

        # Create accounts
        account1 = digital_wallet.add_account(Currency.DOLLAR, 1234567890)
        account2 = digital_wallet.add_account(Currency.EUROS, 9876543210)

        # Add payment methods
        credit_card = CreditCard("PM001", "1234567890123456", "12/25")
        bank_account = BankAccount("PM002", "9876543210", "987654321")
        # digital_wallet.add_payment_method(credit_card)
        # digital_wallet.add_payment_method(bank_account)

        # Deposit funds
        account1.deposit(1000.00)
        account2.deposit(500.00)

        # Transfer funds
        digital_wallet.transfer_funds(account1, account2, 100.00, Currency.DOLLAR)

        # Get transaction history
        transaction_history1 = digital_wallet.get_transaction_history(account1)
        transaction_history2 = digital_wallet.get_transaction_history(account2)

        # Print transaction history
        print("Transaction History for Account 1:")
        for transaction in transaction_history1:
            print(f"Transaction ID: {transaction.id}")
            print(f"Amount: {transaction.amount} {transaction.currency}")
            print(f"Timestamp: {transaction.timestamp}")
            print()

        print("Transaction History for Account 2:")
        for transaction in transaction_history2:
            print(f"Transaction ID: {transaction.id}")
            print(f"Amount: {transaction.amount} {transaction.currency}")
            print(f"Timestamp: {transaction.timestamp}")
            print()

if __name__ == "__main__":
    DigitalWalletDemo.run()