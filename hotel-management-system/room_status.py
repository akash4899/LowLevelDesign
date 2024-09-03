from enum import Enum

class RoomStatus(Enum):
    AVAILABLE = 'Available'
    BOOKED = 'Booked'
    OCCUPIED = 'Occupied'