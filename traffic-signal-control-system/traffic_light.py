from signal import Signal

from threading import Lock

class TrafficLight:

    def __init__(self, id, red_duration, yellow_duration, green_duration):
        self.id = id
        self.road = {}
        self.curr_signal = Signal.RED
        self.red_duration = red_duration
        self.green_duration = green_duration
        self.yellow_duration = yellow_duration
        self.lock = Lock()

    def change_signal(self, signal):
        with self.lock:
            self.curr_signal = signal
            self.notify_road()

    def notify_road(self):
        pass