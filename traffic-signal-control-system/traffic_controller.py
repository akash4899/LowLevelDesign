from traffic_light import TrafficLight
from threading import Lock
import threading
import time
from signal import Signal

class TrafficController:
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance.roads = {}
        return cls._instance

    @classmethod
    def get_instance(cls):
        return cls()

    def add_road(self, road):
        self.roads[road.id] = road

    def remove_road(self, road_id):
        self.roads.pop(road_id, None)

    def start_traffic_control(self):
        for road in self.roads.values():
            traffic_light = road.get_traffic_light()
            threading.Thread(target=self._control_traffic_light, args=(traffic_light,), daemon=True).start()


    def _control_traffic_light(self, traffic_light: TrafficLight):
        while True:
            try:
                time.sleep(traffic_light.red_duration / 1000)  # Convert to seconds
                traffic_light.change_signal(Signal.GREEN)
                time.sleep(traffic_light.green_duration / 1000)
                traffic_light.change_signal(Signal.YELLOW)
                time.sleep(traffic_light.yellow_duration / 1000)
                traffic_light.change_signal(Signal.RED)
            except Exception as e:
                print(f"Error in traffic light control: {e}")

    def handle_emergency(self, traffic_light_id):
        pass

