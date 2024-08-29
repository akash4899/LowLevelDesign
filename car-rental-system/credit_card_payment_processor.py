from payment_processor import PaymentProcessor

class CreditCardPaymentProcessor(PaymentProcessor):
    def process_payment(self, *args):
        return True