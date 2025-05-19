------Creation of table Product------
CREATE TABLE Product (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Category VARCHAR(50),
    Price INT,
    StockQuantity INT,
    Supplier VARCHAR(100)
);

select * from Product;  ---View table---
 
----Inserting the values in table----
INSERT INTO Product (ProductID, ProductName, Category, Price, StockQuantity, Supplier) VALUES
(1, 'Laptop', 'Electronics', 70000, 50, 'TechMart'),
(2, 'Office Chair', 'Furniture', 5000, 100, 'HomeComfort'),
(3, 'Smartwatch', 'Electronics', 15000, 200, 'GadgetHub'),
(4, 'Desk Lamp', 'Lighting', 1200, 300, 'BrightLife'),
(5, 'Wireless Mouse', 'Electronics', 1500, 250, 'GadgetHub');

select * from Product;    ---View table---

---Insert a product named "Gaming Keyboard" under the "Electronics" category, priced at 3500, with 150 units in stock, supplied by "TechMart".---
INSERT INTO Product (ProductID, ProductName, Category, Price, StockQuantity, Supplier) VALUES
(6, 'Gaming Keyboard', 'Electronics', 3500, 150, 'TechMart');

select * from Product;    ---View table---

---Increase the price of all Electronics products by 10%.---
Update Product
set price = Price * 1.10
where Category='Electronics';

select * from Product;     ---View table---

---Remove the product with the ProductID = 4 (Desk Lamp).---
Delete from Product
where ProductID = 4;

select * from Product;     ---View table---

---Display all products sorted by Price in descending order.---
SELECT * FROM Product
ORDER BY Price DESC;

