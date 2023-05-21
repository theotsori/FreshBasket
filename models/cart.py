from models import Product

class Cart:
    def __init__(self, cart_id, user_id):
        self.cart_id = cart_id
        self.user_id = user_id
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)
