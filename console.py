#!/usr/bin/python3

import mysql.connector

class User:
    def __init__(self, id, name, email, password, phone):
        self.user_id = id
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone


class Product:
    def __init__(self, id, name, description, price, image, category):
        self.product_id = id
        self.name = name
        self.description = description
        self.price = price
        self.image = image
        self.category = category


class Cart:
    def __init__(self, cart_id, user_id):
        self.cart_id = cart_id
        self.user_id = user_id
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)


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

db_config = {
    'user': 'fresh_dev_db',
    'password': 'fresh_dev_pwd',
    'host': 'localhost',
    'database': 'fresh_basket'
}

def create_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        print("Connected to the database")
        return conn
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
        return None


def close_connection(conn):
    if conn:
        conn.close()
        print("Connection closed")


def fetch_user_by_id(id):
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM users WHERE id = %s"
            cursor.execute(query, (id,))
            user_data = cursor.fetchone()
            if user_data:
                user = User(*user_data)
                return user
            else:
                print("User not found")
        except mysql.connector.Error as err:
            print(f"Error fetching user from the database: {err}")
        finally:
            cursor.close()
            close_connection(conn)
    return None


def fetch_products():
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM products"
            cursor.execute(query)
            products_data = cursor.fetchall()
            products = []
            for product_data in products_data:
                product = Product(*product_data)
                products.append(product)
            return products
        except mysql.connector.Error as err:
            print(f"Error fetching products from the database: {err}")
        finally:
            cursor.close()
            close_connection(conn)
    return []


"""def main():
    # Fetch user by ID
    user = fetch_user_by_id("1")
    if user:
        print(f"User: {user.name}")

    # Fetch products
    products = fetch_products()
    if products:
        print("Available Products:")
        for product in products:
            print(f"- {product.name}: ${product.price}")
"""

def main():
    user = User("1", "John Doe", "john@example.com", "password", "1234567890")
    product1 = Product("1", "Apple", "Fresh red apple", 1.99, "https://example.com/apple.jpg", "Fruits")
    product2 = Product("2", "Banana", "Ripe yellow banana", 0.99, "https://example.com/banana.jpg", "Fruits")
    cart = Cart("1", user.user_id)
    cart.add_product(product1)
    cart.add_product(product2)

    order = Order("1", user.user_id, "processing", 2.98)
    order.add_product(product1)
    order.add_product(product2)

    print(f"User: {user.name}")
    print("Cart:")
    for product in cart.products:
        print(f"- {product.name}: ${product.price}")
    print("Order:")
    for product in order.products:
        print(f"- {product.name}: ${product.price}")
    print(f"Total: ${order.total}")
    print(f"Status: {order.status}")



if __name__ == "__main__":
    main()
