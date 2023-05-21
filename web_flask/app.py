#!/usr/bin/python3

from flask import Flask, jsonify, request, abort
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Example data
products = [
    {"id": 1, "name": "Apples", "price": 0.99},
    {"id": 2, "name": "Bananas", "price": 0.69},
    {"id": 3, "name": "Oranges", "price": 0.79}
]

# Example user data
users = [
    {"id": 1, "username": "user1", "password_hash": generate_password_hash("password1")},
    {"id": 2, "username": "user2", "password_hash": generate_password_hash("password2")}
]

user_cart = {}
user_orders = {}

# Helper functions
def get_user(username):
    for user in users:
        if user['username'] == username:
            return user
    return None

def get_product(product_id):
    for product in products:
        if product['id'] == product_id:
            return product
    return None

# Authentication routes
@app.route('/api/auth/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    if not username or not password:
        abort(400, 'Please provide a username and password')
    user = get_user(username)
    if not user or not check_password_hash(user['password_hash'], password):
        abort(401, 'Invalid username or password')
    return jsonify({'message': 'Login successful'})

# API routes
@app.route('/api/products', methods=['GET', 'POST'])
def products_route():
    if request.method == 'GET':
        return jsonify(products)
    elif request.method == 'POST':
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            abort(401, 'Authorization header missing')
        auth_token = auth_header.split(' ')[1]
        if auth_token != 'secret_token':
            abort(401, 'Invalid authorization token')
        new_product = request.json
        products.append(new_product)
        return jsonify(new_product), 201

@app.route('/api/cart', methods=['GET', 'POST', 'DELETE'])
def cart_route():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        abort(401, 'Authorization header missing')
    auth_token = auth_header.split(' ')[1]
    if auth_token != 'secret_token':
        abort(401, 'Invalid authorization token')
    username = request.args.get('user')
    if not username:
        abort(400, 'Please provide a username')
    if request.method == 'GET':
        cart = user_cart.get(username, [])
        return jsonify(cart)
    elif request.method == 'POST':
        product_id = request.json.get('product_id')
        quantity = request.json.get('quantity', 1)
        product = get_product(product_id)
        if not product:
            abort(404, 'Product not found')
        if quantity <= 0:
            abort(400, 'Quantity must be positive')
        if username not in user_cart:
            user_cart[username] = []
        for item in user_cart[username]:
            if item['product_id'] == product_id:
                item['quantity'] += quantity
                break
        else:
            user_cart[username].append({'product_id': product_id, 'name': product['name'], 'price': product['price'], 'quantity': quantity})
        return jsonify({'message': 'Product added to cart'}
