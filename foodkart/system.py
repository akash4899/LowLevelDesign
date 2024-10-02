from user import User
from restaurant import Restaurant
from food_item import FoodItem
from threading import Lock
from review import Review

class System:
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls.users = {}
                cls.restaurants = {}
                cls.reviews = []
                cls.current_user = None
            return cls._instance

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls()
        return cls._instance

    def register_user(self, name, gender, phone_number, pincode):
        self.users[phone_number] = User(name, gender, phone_number, pincode)
        return self.users.get(phone_number)

    def register_restaurant(self, name, pin_codes, food_name, food_price, quantity):
        food_item = FoodItem(food_name, food_price, quantity)

        self.restaurants[name] = Restaurant(name, pin_codes, food_item, self.current_user)
        return self.restaurants[name]

    def login_user(self, phone_number):
        if self.users.get(phone_number):
            self.current_user = self.users.get(phone_number)

    def price_fun(self, restaurant):
        return restaurant.food_item.price

    def rating(self, restaurant):
        return restaurant.rating
    def show_restaurant(self, strategy):
        restaurants = []
        for restaurant in self.restaurants.values():
            #print(restaurant)
            for location in restaurant.pin_codes:
                #print(location)
                if location == self.current_user.pincode:
                    restaurants.append(restaurant)

        if strategy.lower() == "price":
            restaurants = sorted(restaurants, key=self.price_fun)
        else:
            restaurants = sorted(restaurants, key=self.rating)
        for restaurant in restaurants:
            print(f"{restaurant.name} {restaurant.food_item.name}")


    def place_order(self, restaurant, quantity):
        # print("*****************************")
        # print(self.current_user.name)
        # print((restaurant.name))
        for location in restaurant.pin_codes:
            # print(location)
            if self.current_user.pincode == location:
                print(self.current_user.pincode)
                print(location)
                restaurant.place_order(quantity)
                return

        #print("Order cant be placed.")

    def create_review(self, restaurant, rating, description):
        review = Review(rating, description)
        restaurant.add_review(review)
        self.current_user.add_review(review)

    def update_quantity(self, restaurant, quantity):
        if restaurant.owner == self.current_user:
            restaurant.update_quantity(quantity)
        else:
            print("Not allowed")

    def update_location(self, restaurant, location):
        if restaurant.owner == self.current_user:
            restaurant.update_quantity(location)
        else:
            print("Not allowed")
