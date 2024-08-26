from message import Message


class Topic:
    def __init__(self, name):
        self.name = name
        self.messages = []
        self.subscribers = []

    def add_message(self, msg):
        print("Message is in T1")
        self.messages.append(msg)
        self.send_message(msg)
        print("Message sent to subscriber.")

    def send_message(self, msg):
        for subscriber in self.subscribers:
            subscriber.message(msg)

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)

    def get_subscribers(self):
        for subscriber in self.subscribers:
            print(f"{subscriber.name}")