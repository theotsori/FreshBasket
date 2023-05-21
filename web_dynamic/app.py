#!/usr/bin/python3

from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection
db_config = {
    'host': 'localhost',
    'user': 'fresh_dev_db',
    'password': 'fresh_dev_pwd',
    'database': 'fresh_basket'
}

# Create a cursor to interact with the database
cursor = None

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

        # Insert the user data into the database
        insert_query = "INSERT INTO User (Name, Email, Password, Phone) VALUES (%s, %s, %s, %s)"
        user_data = (name, email, password, phone)
        cursor.execute(insert_query, user_data)

        # Commit the changes
        cnx.commit()

        # Close the cursor and connection
        cursor.close()
        cnx.close()

        # Return a response
        return 'User signed up successfully'
    else:
        return render_template('signup.html')

if __name__ == '__main__':
    app.run()
