class User:
    def __init__(self, id, name, contact_number, email, password):
        self.id = id
        self.name = name
        self.contact_number = contact_number
        self.email = email
        self.password = password
        self.accounts = []
        self.payment_methods = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_name(self):
        return self.name

    def get_contact_number(self):
        return self.contact_number

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password
        print("Password Updated.")

    def set_email(self, email):
        self.email = email
        print("Email changed.")

    def add_payment_method(self, payment_method):
        self.payment_methods.append(payment_method)
        print("Added payment method.")

    def remove_payment_method(self, payment_method):
        self.payment_methods.remove(payment_method)
        print("Payment Method removed.")