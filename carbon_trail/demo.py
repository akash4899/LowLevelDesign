from publisher import Publisher
from subscriber import Subscriber
from notification_system import NotificationSystem

class Demo:
    @staticmethod
    def run():
        system = NotificationSystem()


        publisher1 = Publisher("Pub1")
        publisher2 = Publisher("Pub2")
        publisher3 = Publisher("Pub3")

        system.add_publisher(publisher1.publisher_id, publisher1)
        system.add_publisher(publisher2.publisher_id, publisher2)
        system.add_publisher(publisher3.publisher_id, publisher3)

        subscriber = Subscriber("Sub1")
        subscriber2 = Subscriber("Sub2")

        system.add_subscriber(subscriber.subscriber_id, subscriber)
        system.add_subscriber(subscriber2.subscriber_id, subscriber2)

        publishers = [publisher1.publisher_id, publisher2.publisher_id, publisher3.publisher_id]
        webhook = "this is the webhook"
        system.subscribe(subscriber.subscriber_id, publishers, webhook)
        system.subscribe(subscriber2.subscriber_id, publisher3.publisher_id, "Carbontrail webhook")

        system.publish_message(publisher1.publisher_id, "Helllo from pub1.")
        system.publish_message(publisher3.publisher_id, "Hello from pub3.")


if __name__ == '__main__':
    Demo.run()

