from flask import Blueprint, render_template, session, redirect, url_for
import mysql.connector

bp = Blueprint('checkout', __name__)

@bp.route('/checkout', methods=['GET', 'POST'])
def checkout():
    # Check if the user is authenticated
    if 'email' not in session:
        return redirect(url_for('signin'))

    # Connect to the MySQL database
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()

    # Retrieve cart data for the user from the database
    select_query = """
    SELECT P.Id, P.Name, P.Description, P.Price, P.Image, P.Category
    FROM CartProduct CP
    JOIN Product P ON CP.ProductId = P.Id
    JOIN Cart C ON CP.CartId = C.Id
    JOIN User U ON C.UserId = U.Id
    WHERE U.Email = %s
    """
    cursor.execute(select_query, (session['email'],))
    cart_products = cursor.fetchall()

    # Calculate the total price of the cart
    total_query = """
    SELECT SUM(P.Price)
    FROM CartProduct CP
    JOIN Product P ON CP.ProductId = P.Id
    JOIN Cart C ON CP.CartId = C.Id
    JOIN User U ON C.UserId = U.Id
    WHERE U.Email = %s
    """
    cursor.execute(total_query, (session['email'],))
    total_price = cursor.fetchone()[0]

    # Retrieve shipping info from database
    select_shipping_query = """
    SELECT * FROM Shipping
    INNER JOIN User ON Shipping.UserId = User.Id
    WHERE User.Email = %s
    """
    cursor.execute(select_shipping_query, (session['email'],))
    shipping_info = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    cnx.close()

    # Render the template and pass the cart data to it
    return render_template('checkout.html',
                           cart_products=cart_products,
                           total_price=total_price,
                           shipping_info=shipping_info)