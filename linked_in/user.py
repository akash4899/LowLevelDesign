from profile import Profile
from connection import Connection

class User:
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.profile = None
        self.connections = []
        self.sent_messages = []
        self.inbox = []

    def set_profile(self, profile):
        self.profile = profile

    def send_message(self, user):
        pass

    def send_connection(self, user):
        pass

    def accept_connection_request(self, connection):
        pass
