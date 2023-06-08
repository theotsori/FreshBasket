from flask import Blueprint, render_template, request, redirect, url_for
import mysql.connector
from config import db_config

bp = Blueprint('signup', __name__)

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Retrieve the form data
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Connect to the MySQL database
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()

        # Check if the email is already registered
        select_query = "SELECT * FROM User WHERE Email = %s"
        cursor.execute(select_query, (email,))
        user = cursor.fetchone()

        if user:
            # Email already exists
            error = 'Email is already registered'
            return render_template('signup.html', error=error)
        else:
            # Insert the new user into the database
            insert_query = "INSERT INTO User (Name, Email, Password) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (name, email, password))
            cnx.commit()

            # Close the cursor and connection
            cursor.close()
            cnx.close()

            # Redirect to the sign-in page
            return redirect(url_for('signin.signin'))
    else:
        return render_template('signup.html')
