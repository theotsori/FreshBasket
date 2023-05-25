#!/usr/bin/python3

from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import mysql.connector

app = Flask(__name__)
app.secret_key = 'my_secret_key'

# Configure MySQL connection
db_config = {
    'host': 'localhost',
    'user': 'fresh_dev_db',
    'password': 'fresh_dev_pwd',
    'database': 'fresh_basket'
}


# Route for home page
@app.route('/')
@app.route('/home')
def home():
    # Check if the user is authenticated
    if 'email' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('signin'))


# Route for recipe
@app.route('/recipe')
def recipe():
    return render_template('recipe.html')


# Route for the product page
@app.route('/products')
def products():
    # Connect to the MySQL database
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()

    # Retrieve product data from the database
    cursor.execute("SELECT * FROM Product")
    products = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    cnx.close()

    # Render the template and pass the product data to it
    return render_template('shop.html', products=products)


@app.route('/cart', methods=['GET', 'POST'])
def cart():
    if request.method == 'POST':
        product_id = request.form['product_id']
        cart_id = get_cart_id()  # Retrieve the cart ID for the current user

        # Add the selected product to the cart
        if cart_id is not None:
            cnx = mysql.connector.connect(**db_config)
            cur = cnx.cursor()
            cur.execute("INSERT INTO CartProduct (CartId, ProductId) VALUES (%s, %s)", (cart_id, product_id))
            cnx.commit()
            cur.close()
            cnx.close()

        return redirect(url_for('cart'))

    # Retrieve the cart items for the current user
    cart_id = get_cart_id()
    cnx = mysql.connector.connect(**db_config)
    cur = cnx.cursor()
    cur.execute(
        "SELECT cp.CartId, p.Name, p.Description, p.Price, p.Image FROM CartProduct cp JOIN Product p ON cp.ProductId = p.Id WHERE cp.CartId = %s",
        (cart_id,))
    cart_items = cur.fetchall()
    cur.close()
    cnx.close()

    # Retrieve the cart count for the current user
    cart_count = get_cart_count()

    return render_template('cart.html', cart_items=cart_items, cart_count=cart_count)


@app.route('/cart/count')
def cart_count():
    # Retrieve the cart count from the database or session
    count = get_cart_count()  # Implement this function to fetch the cart count

    # Return the cart count as JSON response
    return jsonify(cart_count=count)


@app.route('/cart/add', methods=['POST'])
def add_to_cart():
    product_id = request.form['product_id']
    cart_id = get_cart_id()  # Retrieve the cart ID for the current user

    # Add the selected product to the cart
    if cart_id is not None:
        cnx = mysql.connector.connect(**db_config)
        cur = cnx.cursor()
        cur.execute("INSERT INTO CartProduct (CartId, ProductId) VALUES (%s, %s)", (cart_id, product_id))
        cnx.commit()
        cur.close()
        cnx.close()

    # Return the updated cart count as JSON response
    count = get_cart_count()
    return jsonify(cart_count=count)


@app.route('/cart/remove', methods=['POST'])
def remove_from_cart():
    product_id = request.form['product_id']
    cart_id = get_cart_id()  # Retrieve the cart ID for the current user

    # Remove the selected product from the cart
    if cart_id is not None:
        cnx = mysql.connector.connect(**db_config)
        cur = cnx.cursor()
        cur.execute("DELETE FROM CartProduct WHERE CartId = %s AND ProductId = %s", (cart_id, product_id))
        cnx.commit()
        cur.close()
        cnx.close()

    # Return the updated cart count as JSON response
    count = get_cart_count()
    return jsonify(cart_count=count)


@app.route('/cart/checkout', methods=['POST'])
def checkout():
    cart_id = get_cart_id()  # Retrieve the cart ID for the current user
    total_amount = calculate_total_amount(cart_id)  # Calculate the total amount of the order

    # Create a new order
    cnx = mysql.connector.connect(**db_config)
    cur = cnx.cursor()
    cur.execute("INSERT INTO `Order` (UserId, Status, Total) VALUES (%s, %s, %s)", (get_user_id(), 'pending', total_amount))
    order_id = cur.lastrowid

    # Move cart items to the order
    cur.execute("INSERT INTO OrderProduct (OrderId, ProductId) SELECT %s, ProductId FROM CartProduct WHERE CartId = %s", (order_id, cart_id))

    # Clear the cart
    cur.execute("DELETE FROM CartProduct WHERE CartId = %s", (cart_id,))

    cnx.commit()
    cur.close()
    cnx.close()

    return redirect(url_for('orders'))


def get_user_id():
    # Retrieve the user ID for the current user (you need to implement this logic)
    user_id = session.get('user_id')
    return user_id


def get_cart_id():
    # Retrieve the cart ID for the current user
    cnx = mysql.connector.connect(**db_config)
    cur = cnx.cursor()
    cur.execute("SELECT Id FROM Cart WHERE UserId = %s", (get_user_id(),))
    cart_row = cur.fetchone()
    cur.close()
    cnx.close()
    if cart_row is not None:
        return cart_row[0]
    else:
        # Handle the case when cart ID is not found
        return None


def get_cart_count():
    # Retrieve the cart ID for the current user
    cart_id = get_cart_id()

    if cart_id is None:
        return 0

    # Connect to the MySQL database
    cnx = mysql.connector.connect(**db_config)
    cur = cnx.cursor()

    # Count the number of items in the cart
    cur.execute("SELECT COUNT(*) FROM CartProduct WHERE CartId = %s", (cart_id,))
    cart_count = cur.fetchone()[0]

    # Close the cursor and connection
    cur.close()
    cnx.close()

    return cart_count


def calculate_total_amount(cart_id):
    # Calculate the total amount of the order
    cnx = mysql.connector.connect(**db_config)
    cur = cnx.cursor()
    cur.execute(
        "SELECT SUM(p.Price) AS total_amount FROM CartProduct cp JOIN Product p ON cp.ProductId = p.Id WHERE cp.CartId = %s",
        (cart_id,))
    total_amount = cur.fetchone()[0]
    cur.close()
    cnx.close()
    return total_amount


@app.route('/orders')
def orders():
    # Retrieve the orders for the current user
    cnx = mysql.connector.connect(**db_config)
    cur = cnx.cursor()
    cur.execute(
        "SELECT op.OrderId, p.Name, p.Description, p.Price, p.Image FROM OrderProduct op JOIN Product p ON op.ProductId = p.Id WHERE op.OrderId IN (SELECT Id FROM `Order` WHERE UserId = %s)",
        (get_user_id(),))
    orders = cur.fetchall()
    cur.close()
    cnx.close()

    return render_template('orders.html', orders=orders)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        phone = request.form.get('phone')

        # Connect to the MySQL database
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()

        # Check if the email already exists in the database
        select_query = "SELECT * FROM User WHERE Email = %s"
        cursor.execute(select_query, (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            # If the email already exists, display an error message
            error_message = 'Email already exists. Please choose a different email.'
            return render_template('signup.html', error_message=error_message)
        else:
            # Insert the user data into the database
            insert_query = "INSERT INTO User (Name, Email, Password, Phone) VALUES (%s, %s, %s, %s)"
            user_data = (name, email, password, phone)
            cursor.execute(insert_query, user_data)

            # Commit the changes
            cnx.commit()

        # Close the cursor and connection
        cursor.close()
        cnx.close()

        # Create a session for the user
        session['email'] = email

        # Redirect to the profile page
        return redirect(url_for('profile'))
    else:
        return render_template('signup.html')


# Route for sign in
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        # Retrieve form data
        email = request.form.get('email')
        password = request.form.get('password')

        # Connect to the MySQL database
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()

        # Verify the user's credentials
        query = "SELECT Email FROM User WHERE Email = %s AND Password = %s"
        cursor.execute(query, (email, password))
        result = cursor.fetchone()

        if result:
            # If credentials are valid, create a session for the user
            session['email'] = email

            # Redirect to the home page
            return redirect(url_for('home'))

        # User not found or invalid credentials
        return render_template('signup.html')

        # Close the cursor and connection
        cursor.close()
        cnx.close()

    # If it's a GET request and the user is already signed in, redirect to the home page
    if 'email' in session:
        return redirect(url_for('home'))

    # If it's a GET request and the user is not signed in, render the sign-in page
    return render_template('signin.html')


@app.route('/profile')
def profile():
    # Check if the user is authenticated (session exists)
    if 'email' in session:
        # Connect to the MySQL database
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()

        # Retrieve user data from the database
        cursor.execute("SELECT * FROM User WHERE Email = %s", (session['email'],))
        user = cursor.fetchone()

        # Close the cursor and connection
        cursor.close()
        cnx.close()

        # Render the template and pass the user data to it
        return render_template('profile.html', user=user)
    else:
        return redirect(url_for('signin'))


# Route for signing out
@app.route('/signout')
def signout():
    # Clear the session
    session.clear()

    # Redirect to the sign-in page
    return redirect(url_for('signin'))


@app.route('/search')
def search():
    # Get the search query from the request's query parameters
    query = request.args.get('query')

    # Check if the query is None or empty
    if not query or query.strip() == '':
        # Handle the case when no query is provided
        return redirect(url_for('products'))

    # Connect to the MySQL database
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()

    # Search for products matching the query
    search_query = "SELECT * FROM Product WHERE Name LIKE %s OR Description LIKE %s"
    pattern = f'%{query}%'
    cursor.execute(search_query, (pattern, pattern))
    products = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    cnx.close()

    # Render the template and pass the product data to it
    return render_template('search_results.html', products=products, query=query)


if __name__ == '__main__':
    app.run(debug=True)
