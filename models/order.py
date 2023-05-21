from models import Product

class Order:
    def __init__(self, order_id, user_id, status, total):
        self.order_id = order_id
        self.user_id = user_id
        self.products = []
        self.status = status
        self.total = total

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)
