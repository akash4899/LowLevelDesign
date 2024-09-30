import uuid
from threading import Lock
from user import User

class UserManager:
    def __init__(self):
        self.users = {}
        self.lock = Lock()

    def add_user(self, name, contact_number, email, password):
        user_id = self.generate_user_id()
        user = User(user_id, name, contact_number, email, password)
        self.users[user_id] = user
        return user

    def generate_user_id(self):
        return f"USR{uuid.uuid4().hex[:8].upper()}"

    def remove_user(self, user_id):
        with self.lock:
            user = self.users.get(user_id)
            if user:
                self.users.pop(user_id)
