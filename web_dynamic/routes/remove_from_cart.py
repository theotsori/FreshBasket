from flask import Blueprint, render_template, session, redirect, url_for
import mysql.connector

bp = Blueprint('remove_from_cart', __name__)

@bp.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    # Check if the user is authenticated
    if 'email' not in session:
        return redirect(url_for('signin'))

    # Get the product ID from the request form
    product_id = request.form.get('product_id')

    # Connect to the MySQL database
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()

    # Retrieve the user's cart ID
    select_cart_query = "SELECT Id FROM Cart WHERE UserId = (SELECT Id FROM User WHERE Email = %s)"
    cursor.execute(select_cart_query, (session['email'],))
    cart_id = cursor.fetchone()[0]

    # Delete the product from the user's cart
    delete_query = "DELETE FROM CartProduct WHERE CartId = %s AND ProductId = %s"
    cursor.execute(delete_query, (cart_id, product_id))

    # Commit the changes
    cnx.commit()

    # Close the cursor and connection
    cursor.close()
    cnx.close()

    # Redirect back to the cart page
    return redirect(url_for('cart'))
