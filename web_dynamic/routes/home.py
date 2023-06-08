from flask import Blueprint, render_template, session, redirect, url_for, session
import mysql.connector

bp = Blueprint('home', __name__)

@bp.route('/home')
def home():
    # Check if the user is authenticated
    if 'email' in session:
        if session['email'] == 'admin@frb.com':
            return redirect(url_for('admin_panel.admin_panel'))
        else:
            # For regular users, continue with the existing functionality
            cart_count = get_cart_count()
            return render_template('index.html', cart_count=cart_count)
    else:
        return redirect(url_for('signin.signin'))

def get_cart_count():
    # Connect to the MySQL database
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()

    # Retrieve the cart count for the user
    select_query = """
    SELECT COUNT(CP.ProductId)
    FROM CartProduct CP
    JOIN Cart C ON CP.CartId = C.Id
    JOIN User U ON C.UserId = U.Id
    WHERE U.Email = %s
    """
    cursor.execute(select_query, (session['email'],))
    cart_count = cursor.fetchone()[0]

    # Close the cursor and connection
    cursor.close()
    cnx.close()

    return cart_count
