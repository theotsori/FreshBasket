-- MySQL dump 10.13  Distrib 8.0.33, for Linux (aarch64)
--
-- Host: localhost    Database: fresh_basket
-- ------------------------------------------------------
-- Server version	8.0.33-0ubuntu0.22.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Cart`
--

DROP TABLE IF EXISTS `Cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Cart` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `UserId` int NOT NULL,
  `ShippingId` int DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `UserId` (`UserId`),
  KEY `ShippingId` (`ShippingId`),
  CONSTRAINT `Cart_ibfk_1` FOREIGN KEY (`UserId`) REFERENCES `User` (`Id`),
  CONSTRAINT `Cart_ibfk_2` FOREIGN KEY (`ShippingId`) REFERENCES `Shipping` (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cart`
--

LOCK TABLES `Cart` WRITE;
/*!40000 ALTER TABLE `Cart` DISABLE KEYS */;
INSERT INTO `Cart` VALUES (1,17,0),(2,18,0),(3,16,0),(5,20,NULL),(6,21,NULL),(7,22,NULL),(8,23,NULL);
/*!40000 ALTER TABLE `Cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CartProduct`
--

DROP TABLE IF EXISTS `CartProduct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CartProduct` (
  `CartId` int NOT NULL,
  `ProductId` int NOT NULL,
  KEY `CartId` (`CartId`),
  KEY `ProductId` (`ProductId`),
  CONSTRAINT `CartProduct_ibfk_1` FOREIGN KEY (`CartId`) REFERENCES `Cart` (`Id`),
  CONSTRAINT `CartProduct_ibfk_2` FOREIGN KEY (`ProductId`) REFERENCES `Product` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CartProduct`
--

LOCK TABLES `CartProduct` WRITE;
/*!40000 ALTER TABLE `CartProduct` DISABLE KEYS */;
INSERT INTO `CartProduct` VALUES (1,8),(1,7),(1,17),(1,14);
/*!40000 ALTER TABLE `CartProduct` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Order`
--

DROP TABLE IF EXISTS `Order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Order` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `UserId` int NOT NULL,
  `Status` varchar(255) NOT NULL DEFAULT 'processing',
  `Total` decimal(10,2) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `UserId` (`UserId`),
  CONSTRAINT `Order_ibfk_1` FOREIGN KEY (`UserId`) REFERENCES `User` (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Order`
--

LOCK TABLES `Order` WRITE;
/*!40000 ALTER TABLE `Order` DISABLE KEYS */;
INSERT INTO `Order` VALUES (4,1,'processing',2089.45),(5,1,'processing',768.47),(6,1,'processing',768.47),(7,1,'processing',218.99),(8,1,'processing',209.48),(9,1,'processing',579.47),(15,18,'processing',2469.96),(16,16,'processing',648.48),(17,16,'processing',889.47),(18,16,'processing',549.48),(19,18,'processing',3372.95),(20,16,'processing',2159.97),(21,16,'processing',119.99),(22,18,'processing',218.99),(23,20,'processing',1389.48),(24,21,'processing',949.46),(25,16,'processing',549.48),(26,16,'processing',119.99),(27,22,'processing',1559.46),(28,16,'processing',4522.89),(29,16,'processing',388.97),(30,16,'processing',218.99),(31,23,'processing',768.47),(32,23,'processing',2584.46);
/*!40000 ALTER TABLE `Order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `OrderProduct`
--

DROP TABLE IF EXISTS `OrderProduct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `OrderProduct` (
  `OrderId` int NOT NULL,
  `ProductId` int NOT NULL,
  KEY `OrderId` (`OrderId`),
  KEY `ProductId` (`ProductId`),
  CONSTRAINT `OrderProduct_ibfk_1` FOREIGN KEY (`OrderId`) REFERENCES `Order` (`Id`),
  CONSTRAINT `OrderProduct_ibfk_2` FOREIGN KEY (`ProductId`) REFERENCES `Product` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `OrderProduct`
--

LOCK TABLES `OrderProduct` WRITE;
/*!40000 ALTER TABLE `OrderProduct` DISABLE KEYS */;
INSERT INTO `OrderProduct` VALUES (8,6),(8,8),(9,16),(9,11),(9,8),(15,11),(15,10),(15,12),(15,6),(16,5),(16,8),(16,7),(17,8),(17,12),(17,17),(18,7),(18,8),(19,8),(19,12),(19,10),(19,11),(19,9),(19,14),(19,5),(20,7),(20,11),(20,10),(21,6),(22,5),(22,6),(23,10),(23,8),(24,16),(24,12),(24,6),(24,8),(25,8),(25,7),(26,6),(27,10),(27,16),(27,8),(27,15),(28,5),(28,6),(28,7),(28,8),(28,9),(28,10),(28,11),(28,12),(28,13),(28,14),(28,15),(28,16),(28,17),(29,5),(29,6),(29,16),(29,15),(30,5),(30,6),(31,5),(31,6),(31,8),(31,7),(32,5),(32,7),(32,10),(32,12),(32,14);
/*!40000 ALTER TABLE `OrderProduct` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Product`
--

DROP TABLE IF EXISTS `Product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Product` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) NOT NULL,
  `Description` varchar(255) NOT NULL,
  `Price` decimal(10,2) NOT NULL,
  `Image` varchar(255) NOT NULL,
  `Category` varchar(255) NOT NULL,
  `product_id` varchar(255) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Product`
--

LOCK TABLES `Product` WRITE;
/*!40000 ALTER TABLE `Product` DISABLE KEYS */;
INSERT INTO `Product` VALUES (5,'Bananas','Deliciously sweet and rich in potassium, bananas are a nutritious and energizing fruit that satisfies your taste buds and supports your active lifestyle.',99.00,'product-images/bananas.jpg','Fruit','3'),(6,'Milk','Milk is a nutrient-rich food that is an excellent source of protein, calcium, and other essential vitamins and minerals.',119.99,'product-images/milk.jpg','Dairy','4'),(7,'Eggs','Nutritious and versatile, these protein-rich gems are perfect for breakfast or baking, adding delicious flavor to your meals.',459.99,'product-images/eggs.jpg','Dairy','5'),(8,'Bread','Wholesome and comforting, bread is a staple food that complements any meal with its soft texture and versatile flavors.',89.49,'product-images/bread.jpg','Bread','6'),(9,'Cheese','Indulge in the delightful world of cheese, a diverse range of flavors and textures that adds a creamy and savory touch to your dishes.',759.00,'product-images/cheese.jpg','Dairy','7'),(10,'Chicken','Tender and protein-packed, chicken is a versatile white meat that offers a lean and delicious option for your everyday meals.',1299.99,'product-images/chicken.jpg','Meat','8'),(11,'Beef','Savor the rich taste of beef, a succulent red meat that brings a hearty and satisfying flavor to your favorite recipes.',399.99,'product-images/beef.jpg','Meat','9'),(12,'Salmon','Dive into the goodness of salmon, a pink fish renowned for its delicate taste and abundant omega-3 fatty acids, promoting a healthy heart and brain.',649.99,'product-images/salmon.jpg','Fish','10'),(13,'Apples','Enjoy the crisp and refreshing nature of apples, a delicious and nutritious fruit that adds a touch of sweetness to your snacks and recipes.',249.99,'product-images/apples.jpg','Fruit','1'),(14,'Oranges','Experience the zesty and invigorating flavors of oranges, a citrus fruit bursting with vitamin C and a refreshing burst of citrusy goodness.',75.49,'product-images/oranges.jpg','Fruit','2'),(15,'Grapes','Enjoy the sweet and refreshing taste of grapes, a versatile fruit that is perfect for snacking or adding to salads and desserts.',79.99,'product-images/grapes.jpg','Fruit','15'),(16,'Tomatoes','Versatile and vibrant, tomatoes are a staple ingredient that adds a tangy and savory touch to your salads, sauces, and more.',89.99,'product-images/tomatoes.jpg','Vegetable','16'),(17,'Strawberries','Sweet and juicy, strawberries are a delightful fruit that brings a burst of flavor to your desserts and snacks.',149.99,'product-images/strawberries.jpg','Fruit','17');
/*!40000 ALTER TABLE `Product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Shipping`
--

DROP TABLE IF EXISTS `Shipping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Shipping` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `UserId` int DEFAULT NULL,
  `Full_Name` varchar(255) DEFAULT NULL,
  `Street_Address` varchar(255) DEFAULT NULL,
  `City` varchar(255) DEFAULT NULL,
  `State_Province` varchar(255) DEFAULT NULL,
  `Postal_Code` varchar(255) DEFAULT NULL,
  `Country` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `UserId` (`UserId`),
  CONSTRAINT `Shipping_ibfk_1` FOREIGN KEY (`UserId`) REFERENCES `User` (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Shipping`
--

LOCK TABLES `Shipping` WRITE;
/*!40000 ALTER TABLE `Shipping` DISABLE KEYS */;
INSERT INTO `Shipping` VALUES (10,17,'Teddy G','Langas','Nakuru','Mombasa','20200','Kenya'),(11,18,'James W','Kiamunyi','Molo','Rift-Valley','20100','Kenya'),(13,20,'John Kelly','Mangu','Kericho','Rift-Valley','011000','South Africa'),(14,21,'Motty Blue','Wall street','New York','Boston','120543','United States'),(31,16,'John Foe','Kiamunyi','Meru','Central','40320','Kenya'),(32,22,'Joe Kamau','Karen','Nairobi','Central','00100','Kenya'),(34,23,'Kate Mambo','Kiamunyi','Mombasa','Mombasa','00500','Kenya');
/*!40000 ALTER TABLE `Shipping` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `Phone` varchar(20) NOT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `unique_email` (`Email`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (11,'Gregory Kibs','gregkibs@example.com','Greg','0741123123'),(12,'Martin Luther','martinluther@example.com','Martin','0712345678'),(13,'Roy Martin','roymartin@example.com','Roy','0106320609'),(14,'Lawrence Kibs','lawrencekibs@example.com','Larry','0792123123'),(15,'Gregory Remmie','gregrem@you.com','Remy','0741321321'),(16,'John Foe','johnfoe@gmail.com','$2b$12$6lafyk5ULE2xwv.FqyzyHuntN8VMwNRkae7mForvet9FgCz/p.0Aq','0790320320'),(17,'Teddy Gift','teddyg@you.com','$2b$12$AH3cEuTI0ru3Amkj3LIVJOp40QTycsjIfT9I9WqQsxsTrezUCiG1a','0790192324'),(18,'James W','wjames@you.com','$2b$12$7OIWlRTvdlnv6UEZ7Y888uwqADlhEHj6b9NOmAtDwkV2ZHt5nUly6','0722123123'),(19,'Gregory Remmie','remmiegreg@you.com','$2b$12$hZGNYxCVEaX7qH.TNt4GhuAgI5rKEDmHE6dFlyseEKU0g5v6GnoNy','0741123123'),(20,'Kelly John','johnkelly@you.com','$2b$12$HqVye1GyzqVucrGFUzeyDOGH.Wy.m8FCMCvbZDUnfzUXkqy4oMoPy','0790234234'),(21,'Motty Blue','mottyb@you.com','$2b$12$7YvOEYT0H2oF8VG9C1UzTeKO62OTWc2niFOczWQd89FoodvO/RCS6','0102030405'),(22,'Joe Kamau','joekamau@gmail.com','$2b$12$IMrW/4bFYS8Orff8MJA2g.AFHK4VAnzV90D7anpWR7rFimMT2ox.C','0790500500'),(23,'Kate Mambo','mambokate@you.com','$2b$12$xKRNgh//QHxoeVqlvEvdceUVjLCl9a4xjwGM7sIm3G91xGf2SwgBC','0790192324');
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-30 23:01:27
