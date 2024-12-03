from threading import Lock


class NotificationSystem:
        _lock = Lock()
        _instance = None
        def __init__(self):
            self.publishers = {}
            self.subscribers = {}
            self.lock = Lock()

        def add_publisher(self, publisher_id, publisher):
            self.publishers[publisher_id] = publisher

        def add_subscriber(self, subscriber_id, subscriber):
            self.subscribers[subscriber_id] = subscriber

        def subscribe(self, subscriber_id, publishers, webhook):
            for publisher in self.publishers.values():
                if publisher.publisher_id in publishers:
                    publisher.add_subscriber(self.subscribers[subscriber_id])
                    self.subscribers[subscriber_id].webhook_mapping[publisher.publisher_id] = webhook



        def publish_message(self, publisher_id, message):
            subscribers = self.publishers[publisher_id].get_subscribers()
            if subscribers is None:
                print("No Subcriber exist.")
                return
            for subscriber in  subscribers:
                print(f"Subscriber ID: {subscriber.subscriber_id}, publisher ID: {publisher_id}, message = {message}, webhook: {subscriber.get_webhook(publisher_id)}")

