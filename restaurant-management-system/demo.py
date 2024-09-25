from restaurant_system import System
from customer import Customer
from item import Item

class Demo:
    @staticmethod
    def run():
        restaurant_system = System.get_instance()
        customer1 = Customer("John", "9990006667")

        item1 = Item(1, "Burger", 50)
        item2 = Item(2, "Soup", 40)

        order = restaurant_system.place_order([item1, item2])
        print(order.order_id)
        print(order.bill.bill_id)
        restaurant_system.pay_bill(order.bill)



if __name__ == '__main__':
    Demo.run()

