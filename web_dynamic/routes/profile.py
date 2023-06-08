from flask import Blueprint, render_template, session, redirect, url_for
import mysql.connector

bp = Blueprint('profile', __name__)

@bp.route('/profile')
def profile():
    # Check if the user is authenticated
    if 'email' in session:
        # Connect to the MySQL database
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()

        # Retrieve the user data from the database
        select_query = "SELECT * FROM User WHERE Email = %s"
        cursor.execute(select_query, (session['email'],))
        user = cursor.fetchone()

        # Close the cursor and connection
        cursor.close()
        cnx.close()

        # Render the template and pass the user data to it
        cart_count = get_cart_count()
        return render_template('profile.html', user=user, cart_count=cart_count)
    else:
        return redirect(url_for('signin'))
