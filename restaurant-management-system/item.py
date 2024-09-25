
class Item:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_item_id(self):
        return self.item_id

    def get_price(self):
        return self.price