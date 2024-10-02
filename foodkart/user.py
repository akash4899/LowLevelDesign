class User:
    def __init__(self, name, gender, phone_number, pincode):
        self.name = name
        self.gender = gender
        self.phone_number = phone_number
        self.pincode = pincode
        self.restaurants = []
        self.reviews = []

    def add_restaurant(self, restaurant):
        self.restaurants.append(restaurant)

    def add_review(self, review):
        self.reviews.append(review)

