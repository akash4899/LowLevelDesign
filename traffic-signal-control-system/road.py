class Road:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.traffic_light = None

    def notify(self):
        print("The signal has changed.")

    def set_traffic_light(self, traffic_light):
        self.traffic_light = traffic_light

    def get_traffic_light(self):
        return self.traffic_light

    def get_id(self):
        return self.id