from flask import Blueprint, render_template, request, session, redirect, url_for
import mysql.connector
from config import db_config

bp = Blueprint('signin', __name__)

@bp.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        # Retrieve the form data
        email = request.form['email']
        password = request.form['password']

        # Connect to the MySQL database
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()

        # Check if the email and password match
        select_query = "SELECT * FROM User WHERE Email = %s AND Password = %s"
        cursor.execute(select_query, (email, password))
        user = cursor.fetchone()

        if user:
            # Email and password match
            session['email'] = email

            # Close the cursor and connection
            cursor.close()
            cnx.close()

            # Redirect to the home page
            return redirect(url_for('home.home'))
        else:
            # Email and password do not match
            error = 'Invalid email or password'
            return render_template('signin.html', error=error)
    else:
        return render_template('signin.html')
