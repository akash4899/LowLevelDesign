
class Subscriber:
    def __init__(self, subscriber_id):
        self.subscriber_id = subscriber_id
        self.webhook_mapping = {}
        print(f"Subscriber with id: {subscriber_id} is created.")

    def add_webhook_mapping(self, publisher_id, webhook):
        self.webhook_mapping[publisher_id] = webhook

    def get_webhook(self, publisher_id):
        return self.webhook_mapping[publisher_id]