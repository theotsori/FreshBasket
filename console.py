#!/usr/bin/python3
"""Main console"""

class User:
    def __init__(self, user_id, name, email, password, phone):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone

    def __str__(self):
        return f"User ID: {self.user_id}\nName: {self.name}\nEmail: {self.email}\nPhone: {self.phone}"


class Product:
    def __init__(self, product_id, name, description, price, image, category):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.image = image
        self.category = category

    def __str__(self):
        return f"Product ID: {self.product_id}\nName: {self.name}\nDescription: {self.description}\nPrice: {self.price}\nImage: {self.image}\nCategory: {self.category}"


class Cart:
    def __init__(self, cart_id, user_id):
        self.cart_id = cart_id
        self.user_id = user_id
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def __str__(self):
        return f"Cart ID: {self.cart_id}\nUser ID: {self.user_id}\nProducts: {', '.join([p.name for p in self.products])}"


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

    def __str__(self):
        return f"Order ID: {self.order_id}\nUser ID: {self.user_id}\nProducts: {', '.join([p.name for p in self.products])}\nStatus: {self.status}\nTotal: {self.total}"


# Example usage:
user = User("1", "John Doe", "john@example.com", "password", "1234567890")
product1 = Product("1", "Apple", "Fresh red apple", 1.99, "https://example.com/apple.jpg", "Fruits")
product2 = Product("2", "Banana", "Ripe yellow banana", 0.99, "https://example.com/banana.jpg", "Fruits")
cart = Cart("1", user.user_id)
cart.add_product(product1)
cart.add_product(product2)

order = Order("1", user.user_id, "processing", 2.98)
order.add_product(product1)
order.add_product(product2)

print("User:")
print(user)
print("\nCart:")
print(cart)
print("\nOrder:")
print(order)
