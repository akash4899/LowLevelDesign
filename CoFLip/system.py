import uuid
from threading import Lock
from user import User
from centre import Centre

class System:
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls.users = {}
                cls.centres = {}
                cls.successful_users = []
        return cls._instance

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls()
        return cls._instance

    def register_user(self, username, preferred_vaccine_type, gender=None):
        user_id = self.generate_user_id()
        user = User(username, gender, preferred_vaccine_type)
        self.users[user_id] = user
        return user

    def register_centre(self, centre_name):
        centre_id = self.generate_centre_id()
        centre = Centre(centre_id, centre_name)
        self.centres[centre_id] = centre
        return centre

    def add_inventory_to_centre(self, centre_id, vaccine_type, quantity):
        centre = self.centres.get(centre_id)
        if centre:
            centre.add_inventory(vaccine_type, quantity)

    def sorting_function(self, item):
        return -item[0], -item[1]

    def get_centres(self, user):
        centres_list = []
        vaccine_type = user.preferred_vaccine_type
        for centre in self.centres.values():
            vaccines = centre.get_vaccine_quantity(vaccine_type)
            bookings = centre.get_number_of_bookings()
            if vaccines:
                centres_list.append([vaccines, bookings, centre.centre_name])
        centres_list = sorted(centres_list, key=self.sorting_function)
        return centres_list

    def book_slot(self, user, center_id):
        centre = self.centres.get(center_id)
        preferred_vaccine = user.preferred_vaccine_type

        if centre.book_slot(user, preferred_vaccine) == 1:
            print("Booking Success.")
            self.successful_users.append(user)
            return True
        return False

    def get_stats(self):
        for centre in self.centres.values():
            # print(centre)
            print(f"{centre.centre_name}")
            for vaccine_type, vaccines in centre.vaccine_inventory.items():
                print(f"{vaccine_type} {vaccines}")
            for user in centre.users:
                print(user.name)

    def generate_user_id(self):
        return f"USR{uuid.uuid4().hex[:8].upper()}"

    def generate_centre_id(self):
        return f"CTR{uuid.uuid4().hex[:8].upper()}"