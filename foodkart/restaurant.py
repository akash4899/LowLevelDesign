class Restaurant:
    def __init__(self, name, pin_codes, food_item, owner):
        self.name = name
        self.pin_codes = pin_codes
        self.food_item = food_item
        self.reviews = []
        self.rating = 0
        self.owner = owner

    def add_review(self, review):
        self.reviews.append(review)
        self.calculate_rating()

    def calculate_rating(self):
        total_rating = 0
        for review in self.reviews:
            print(review)
            # print(review.description)
            total_rating += review.rating

        self.rating = total_rating/len(self.reviews)

    def update_price(self, price):
        self.food_item.price = price

    def update_quantity(self, quantity):
        self.food_item.quantity += quantity
        print(f"{self.name} {self.food_item.name}", end="")
        for pin_code in self.pin_codes:
            print(f" {pin_code} ", end="")

        print(f"{self.food_item.price} {self.food_item.quantity}")

    def update_location(self, pin_codes):
        self.pin_codes = pin_codes
        print(f"{self.name} {self.food_item.name}", end="")
        for pin_code in self.pin_codes:
            # print("here")
            print(f" {pin_code} ", end="")

        print(f"{self.food_item.price} {self.food_item.quantity}")

    def place_order(self, quantity):
        if quantity <= self.food_item.quantity:
            self.food_item.quantity -= quantity
            print("Order placed Successfully.")
        else:
            print("Not enough quantity.")


