# FreshBasket

This code is a Flask web application that implements a simple e-commerce platform. The application allows users to sign up, sign in, view products, add products to their cart, and place orders. It also provides functionalities for searching products, viewing the user profile, and signing out.

## Setup

To run the application, ensure that you have Python 3 and the necessary dependencies installed. You can install the dependencies by running the following command:

`$` pip install flask mysql-connector-python bcrpt requests


Make sure you have a MySQL database set up and the necessary environment variables configured. The following environment variables are used in the code:

- `APP_SECRET_KEY`: The secret key used for session encryption.
- `DB_HOST`: The hostname or IP address of the MySQL database server.
- `DB_USER`: The username to connect to the MySQL database.
- `DB_PASSWORD`: The password for the MySQL database user.
- `DB_DATABASE`: The name of the MySQL database.

After configuring the environment variables, you can start the application by running the following command:

`$` python3 app.py


## Code Structure

The code consists of the following main components:

1. Importing necessary libraries: The code imports the required Flask, MySQL Connector, bcrypt, requests, and os libraries.

2. Setting up Flask: The Flask application is initialized and configured with a secret key retrieved from the environment variables.

3. Database configuration: The MySQL database connection details are retrieved from the environment variables and stored in the `db_config` dictionary.

4. Routes and views: The code defines various routes and view functions that handle different HTTP requests.

   - Home page (`/` or `/home`): Renders the home page with the cart count.
   - Recipe page (`/recipe`): Renders the recipe page with the cart count.
   - Products page (`/products`): Retrieves product data from the database and renders the products page with the product data and cart count.
   - Sign up page (`/signup`): Handles sign up requests, validates the form data, inserts the user data into the database, creates a session for the user, and redirects to the profile page.
   - Sign in page (`/signin`): Handles sign in requests, retrieves the user's hashed password from the database, verifies the password, creates a session for the user if the credentials are valid, and redirects to the home page.
   - Profile page (`/profile`): Renders the user's profile page with user data, shipping information, and cart count.
   - Sign out (`/signout`): Clears the session and redirects to the sign-in page.
   - Search page (`/search`): Handles product search requests, retrieves products matching the search query from the database, and renders the search results page with the product data and cart count.
   - Cart page (`/cart`): Renders the cart page with cart data, total price, and shipping information.
   - Add to cart (`/add_to_cart`): Adds a product to the user's cart by inserting the data into the database.
   - Remove from cart (`/remove_from_cart`): Removes a product from the user's cart by deleting the data from the database.
   - Checkout page (`/checkout`): Renders the checkout page with cart data, total price, and shipping information.
   - Place order (`/place_order`): Handles the order placement by retrieving the user and cart information, calculating the total price, and performing necessary database operations.

5. Helper function: `get_cart_count()`: Retrieves the cart count for the user by querying the database and returns the count.

The code uses the Flask `render_template()` function to render HTML templates and the MySQL Connector library to interact with the MySQL database.

## Conclusion

This is a simple Flask web application that implements a basic e-commerce platform. It provides functionalities for user registration, authentication, product browsing, cart management, and order placement. You can further enhance the application by adding features like payment integration, order history, user reviews, and more.

Feel free to explore the code, make modifications, and customize it according to your requirements. Happy coding!
