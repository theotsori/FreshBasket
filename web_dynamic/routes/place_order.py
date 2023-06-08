from flask import Blueprint, render_template, session, redirect, url_for
import mysql.connector

bp = Blueprint('place_order', __name__)

@bp.route('/place_order', methods=['POST'])
def place_order():
    # Check if the user is authenticated
    if 'email' not in session:
        return redirect(url_for('signin'))

    # Retrieve the user's ID
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()

    # Retrieve the UserId based on the user's email in the session
    select_user_id_query = "SELECT Id FROM User WHERE Email = %s"
    cursor.execute(select_user_id_query, (session['email'],))
    user_id = cursor.fetchone()[0]

    # Retrieve the user's cart ID
    select_cart_query = "SELECT Id FROM Cart WHERE UserId = %s"
    cursor.execute(select_cart_query, (user_id,))
    cart_id = cursor.fetchone()[0]

    # Calculate the total price of the order
    total_query = """
    SELECT SUM(P.Price)
    FROM CartProduct CP
    JOIN Product P ON CP.ProductId = P.Id
    JOIN Cart C ON CP.CartId = C.Id
    JOIN User U ON C.UserId = U.Id
    WHERE U.Id = %s
    """
    cursor.execute(total_query, (user_id,))
    total_price = cursor.fetchone()[0]

    # Insert the order into the database
    insert_order_query = "INSERT INTO `Order` (UserId, Status, Total) VALUES (%s, %s, %s)"
    cursor.execute(insert_order_query, (user_id, 'processing', total_price))
    cnx.commit()
    order_id = cursor.lastrowid

    # Retrieve the products from the user's cart
    select_cart_products_query = "SELECT ProductId FROM CartProduct WHERE CartId = %s"
    cursor.execute(select_cart_products_query, (cart_id,))
    cart_products = cursor.fetchall()

    # Insert the products into the OrderProduct table
    insert_order_product_query = "INSERT INTO OrderProduct (OrderId, ProductId) VALUES (%s, %s)"
    order_product_data = [(order_id, product_id) for product_id, in cart_products]
    cursor.executemany(insert_order_product_query, order_product_data)
    cnx.commit()

    # Remove the products from the user's cart
    delete_cart_products_query = "DELETE FROM CartProduct WHERE CartId = %s"
    cursor.execute(delete_cart_products_query, (cart_id,))

    # Commit the changes
    cnx.commit()

    # Close the cursor and connection
    cursor.close()
    cnx.close()

    # Redirect to the order confirmation page
    return redirect(url_for('order_confirmation', order_id=order_id))
