-- Create the database
CREATE DATABASE fresh_basket;

-- Switch to the newly created database
USE fresh_basket;

-- Create the User table
CREATE TABLE User (
    Id INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    Password VARCHAR(255) NOT NULL,
    Phone VARCHAR(20) NOT NULL
);

-- Create the Product table
CREATE TABLE Product (
    Id INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Description VARCHAR(255) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    Image VARCHAR(255) NOT NULL,
    Category VARCHAR(255) NOT NULL
);

-- Create the Cart table
CREATE TABLE Cart (
    Id INT PRIMARY KEY AUTO_INCREMENT,
    UserId INT NOT NULL,
    FOREIGN KEY (UserId) REFERENCES User(Id)
);

-- Create the CartProduct table (to represent the many-to-many relationship between Cart and Product)
CREATE TABLE CartProduct (
    CartId INT NOT NULL,
    ProductId INT NOT NULL,
    FOREIGN KEY (CartId) REFERENCES Cart(Id),
    FOREIGN KEY (ProductId) REFERENCES Product(Id)
);

-- Create the Order table
CREATE TABLE `Order` (
    Id INT PRIMARY KEY AUTO_INCREMENT,
    UserId INT NOT NULL,
    Status VARCHAR(255) NOT NULL,
    Total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (UserId) REFERENCES User(Id)
);

-- Create the OrderProduct table
CREATE TABLE OrderProduct (
    OrderId INT NOT NULL,
    ProductId INT NOT NULL,
    FOREIGN KEY (OrderId) REFERENCES `Order`(Id),
    FOREIGN KEY (ProductId) REFERENCES Product(Id)
);