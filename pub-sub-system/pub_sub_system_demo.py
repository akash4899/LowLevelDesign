from pub_sub_system import PubSubSystem
class Demo:
    @classmethod
    def run(cls):
        pub_sub_system = PubSubSystem.get_instance()

        p1 = pub_sub_system.add_publisher("P1")

        #print(p1.name)
        t1 = pub_sub_system.add_topic_to_publisher("T1", p1)
        s1 = pub_sub_system.add_subscriber("S1", t1)
        m1 = pub_sub_system.publish_message("M1", t1, p1)


        t1.get_subscribers()


if __name__ == "__main__":
    Demo.run()

