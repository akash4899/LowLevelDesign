from product import Product

class Rack:
    def __init__(self, id):
        self.id = id
        self.products_list = []

    def fill_products(self, products):
        for product in products:
            self.products_list.append(product)