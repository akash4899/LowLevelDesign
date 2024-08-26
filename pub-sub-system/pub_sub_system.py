from message import Message
from topic import Topic
from publisher import Publisher
from subscriber import Subcriber
from threading import Lock
class PubSubSystem:
    _lock = Lock()
    _instance = None
    def __init__(self):
        with PubSubSystem._lock:
            if PubSubSystem._instance is None:
                PubSubSystem._instance = self
                self.publishers = []
                self.subscibers = []
            else:
                return "This is a singleton class. You cannot create another instance."

    @classmethod
    def get_instance(cls):
        if cls._instance is not None:
            return cls._instance
        return PubSubSystem()

    def add_subscriber(self, subscriber_name, topic: Topic):
        subscriber =  Subcriber(subscriber_name)
        self.subscibers.append(subscriber)
        topic.add_subscriber(subscriber)
        return subscriber

    def add_publisher(self, publisher_name):
        publisher = Publisher(publisher_name)
        self.publishers.append(publisher)
        return publisher

    def add_topic_to_publisher(self, topic_name, publisher):
        topic = Topic(topic_name)
        publisher.add_topic(topic)
        return topic

    def publish_message(self, message_content, topic_name, publisher):
        message = Message(message_content)
        publisher.publish_message(topic_name, message)


    def get_subscribers(self):
        for subscriber in self.subscribers:
            print(f"{subscriber.name}")

    def get_publishers(self):
        for publisher in self.publishers:
            print(f"{publisher.name}")

