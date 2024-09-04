from threading import Lock
from message import Message
from user import User
from typing import List, Dict
from notification import Notification, NotificationType
import  uuid
from connection import Connection
from datetime import datetime
class LinkedInSystem:
    _instance =  None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance.users = Dict[str, User] = {}
                cls._instance.notifications = Dict[str, Notification] = {}
            return cls._instance

    @classmethod
    def get_instance(cls):
        return cls()

    def register_user(self, user: User):
        self.users[user.id] = user

    def login_user(self, email: str, password: str) -> Optional[User]:
        for user in self.users.values():
            if user.email == email and user.password == password:
                return user
        return None

    def send_connection_request(self, sender: User, receiver: User):
        connection = Connection(sender, datetime.now())
        receiver.connections.append(connection)
        notification = Notification(self._generate_notification_id(), receiver,
                                    NotificationType.CONNECTION_REQUEST,
                                    f"New connection request from {sender.name}",
                                    datetime.now())
        self._add_notification(receiver.id, notification)

    def accept_connection_request(self, user: User, connection_user: User):
        for connection in user.connections:
            if connection.user == connection_user:
                user.connections.append(Connection(connection_user, datetime.now()))
                break



    def send_message(self, sender: User, receiver: User, content: str):
        message = Message(self._generate_message_id(), sender, receiver, content, datetime.now())
        receiver.inbox.append(message)
        sender.sent_messages.append(message)
        notification = Notification(self._generate_notification_id(), receiver,
                                    NotificationType.MESSAGE,
                                    f"New message from {sender.name}",
                                    datetime.now())
        self._add_notification(receiver.id, notification)

    def _add_notification(self, user_id: str, notification: Notification):
        if user_id not in self.notifications:
            self.notifications[user_id] = []
        self.notifications[user_id].append(notification)

    def get_notifications(self, user_id: str) -> List[Notification]:
        return self.notifications.get(user_id, [])

    def _generate_notification_id(self) -> str:
        return str(uuid.uuid4())

    def _generate_message_id(self) -> str:
        return str(uuid.uuid4())

    def accept_connection_request(self, user: User, connection_user: User):
        for connection in user.connections:
            if connection.user == connection_user:
                user.connections.append(Connection(connection_user, datetime.now()))
                break

    def search_users(self, keyword: str) -> List[User]:
        return [user for user in self.users.values() if keyword.lower() in user.name.lower()]