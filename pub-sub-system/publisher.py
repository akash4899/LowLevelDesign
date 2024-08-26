from topic import Topic
from message import Message

class Publisher:
    def __init__(self, name):
        self.name = name
        self.topics = []

    def add_topic(self, topic):
        self.topics.append(topic)

    def remove_topic(self, topic):
        if topic in self.topics:
            self.topics.remove(topic)

    def publish_message(self, topic: Topic, message):
        if topic in self.topics:
            topic.add_message(message)
            print(f"The message is published in topic {topic.name}")

