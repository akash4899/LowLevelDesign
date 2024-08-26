
class Subcriber:
    def __init__(self, name):
        self.name = name
        self.messages = []

    def get_name(self):
        return self.name

    def message(self, msg):
        self.messages.append(msg)
        print(f"Message received. The content is {msg.content}")

    def subscribe(self, topic):
        topic.add_subscriber(self)
