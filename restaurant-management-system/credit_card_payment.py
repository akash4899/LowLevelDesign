from payment import Payment
from bill import PaymentStatus
class CreditCardPayment(Payment):

    def pay(self):
        self.bill.payment_status = PaymentStatus.PAID
        print("Doing Payment through credit card....")
        print("Payment done.")