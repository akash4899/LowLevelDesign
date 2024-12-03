class Publisher:
    def __init__(self, publisher_id):
        self.publisher_id = publisher_id
        self.messages = []
        self.subscribers = []
        print(f"Publisher with id: {publisher_id} is created.")

    def publish_message(self, message):
        pass

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def get_subscribers(self):
        return self.subscribers