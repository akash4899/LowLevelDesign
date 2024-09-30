from payment_method import Payment_Method

class CreditCard(Payment_Method):
    def __init__(self, card_number, cvv, card_holder):
        self.card_number = card_number
        self.cvv = cvv
        self.card_holder = card_holder

    def process_payment(self, amount):
        print("Payment processed through credit card.")
        return 1