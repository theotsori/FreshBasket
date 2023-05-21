from console import Product
import mysql.connector

# Establish a connection to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="fresh_dev_db",
    password="fresh_dev_pwd",
    database="fresh_basket"
)

# Create a cursor object to execute SQL queries
cursor = db.cursor()

# Alter the table to add the 'product_id' column
alter_query = "ALTER TABLE Product ADD COLUMN product_id VARCHAR(255) NOT NULL"
cursor.execute(alter_query)


# Example usage:
product1 = Product("1", "Apple", "Fresh red apple", 1.99, "https://example.com/apple.jpg", "Fruits")
product2 = Product("2", "Banana", "Ripe yellow banana", 0.99, "https://example.com/banana.jpg", "Fruits")

# Insert product1 into the database
insert_query = "INSERT INTO Product (product_id, name, description, price, image, category) VALUES (%s, %s, %s, %s, %s, %s)"
product1_data = (product1.product_id, product1.name, product1.description, product1.price, product1.image, product1.category)
cursor.execute(insert_query, product1_data)
db.commit()

# Insert product2 into the database
insert_query = "INSERT INTO Product (product_id, name, description, price, image, category) VALUES (%s, %s, %s, %s, %s, %s)"
product2_data = (product2.product_id, product2.name, product2.description, product2.price, product2.image, product2.category)
cursor.execute(insert_query, product2_data)
db.commit()

# Close the cursor and database connection
cursor.close()
db.close()