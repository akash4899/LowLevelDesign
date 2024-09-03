from abc import ABC, abstractmethod
from room_status import RoomStatus

class Room(ABC):
    @abstractmethod
    def __init__(self, room_number):
        pass

    @abstractmethod
    def book_room(self):
        pass

    @abstractmethod
    def check_in(self):
        pass

    @abstractmethod
    def check_out(self):
        pass

    @abstractmethod
    def get_room_number(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

    def get_room_status(self):
        pass

