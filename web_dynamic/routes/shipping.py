from flask import Blueprint, render_template, session, redirect, url_for
import mysql.connector

bp = Blueprint('shipping', __name__)

@bp.route('/shipping', methods=['GET', 'POST'])
def shipping():
    # Check if the user is authenticated
    if 'email' not in session:
        return redirect(url_for('signin'))

    if request.method == 'POST':
        if 'delete_shipping' in request.form:
            # Delete shipping information
            shipping_id = request.form.get('delete_shipping')
            # Connect to the MySQL database
            cnx = mysql.connector.connect(**db_config)
            cursor = cnx.cursor()
            
            # Delete the shipping information from the database
            delete_shipping_query = "DELETE FROM Shipping WHERE Id = %s"
            cursor.execute(delete_shipping_query, (shipping_id,))
            cnx.commit()

            # Close the cursor and connection
            cursor.close()
            cnx.close()

            # Redirect the user back to the shipping page
            return redirect(url_for('shipping'))

        else:
            # Retrieve shipping information from the form
            full_name = request.form.get('full_name')
            street_address = request.form.get('street_address')
            city = request.form.get('city')
            state_province = request.form.get('state_province')
            postal_code = request.form.get('postal_code')
            country = request.form.get('country')

            # Connect to the MySQL database
            cnx = mysql.connector.connect(**db_config)
            cursor = cnx.cursor()

            # Retrieve the user's ID
            select_user_query = "SELECT Id FROM User WHERE Email = %s"
            cursor.execute(select_user_query, (session['email'],))
            user_id = cursor.fetchone()[0]

            # Insert the shipping information into the shipping table
            insert_shipping_query = """
            INSERT INTO Shipping (UserId, Full_Name, Street_Address, City, State_Province, Postal_Code, Country)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            shipping_data = (user_id, full_name, street_address, city, state_province, postal_code, country)
            cursor.execute(insert_shipping_query, shipping_data)
            cnx.commit()

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

            # redirect the user back to the shipping page
            return render_template('shipping.html', shipping_info=shipping_info)

    # If it's a GET request, render the shipping information form
    # Retrieve existing shipping info from database
    # Connect to the MySQL database
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()
    
    # Retrieve shipping info from the database
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

    return render_template('shipping.html', shipping_info=shipping_info)
