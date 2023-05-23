#!/usr/bin/python3

from flask import Flask, render_template, request, session, redirect, url_for
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

        try:
            # Verify the user's credentials
            query = "SELECT Email FROM User WHERE Email = %s AND Password = %s"
            cursor.execute(query, (email, password))
            result = cursor.fetchone()

            if result:
                # If credentials are valid, create a session for the user
                session['email'] = email

                # Redirect to the home page
                return redirect(url_for('home'))

            # If credentials are invalid, display an error message
            error_message = 'Invalid credentials. Please try again.'
            return render_template('signin.html', error_message=error_message)

        except Exception as e:
            # Handle any exceptions that may occur during database operations
            error_message = 'An error occurred while processing your request.'
            # Log the error for debugging purposes
            print(f"Error: {str(e)}")
            return render_template('signin.html', error_message=error_message)

        finally:
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

        # Retrieve the user's information from the database
        select_query = "SELECT * FROM User WHERE Email = %s"
        cursor.execute(select_query, (session['email'],))
        user_data = cursor.fetchone()

        # Close the cursor and connection
        cursor.close()
        cnx.close()

        # Pass the user's information to the template
        return render_template('profile.html', user=user_data)
    else:
        # If the user is not authenticated, redirect them to the sign-in page
        return redirect(url_for('signin'))


@app.route('/signout')
def signout():
    # Clear the user's session
    session.pop('email', None)

    # Redirect to the home page or any other appropriate page
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()
