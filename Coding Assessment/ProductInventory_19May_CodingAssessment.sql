use Product;   --DB Name is Product--

--create the table ProductInventroy(Schema)--
CREATE TABLE ProductInventory (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(50),
    Category VARCHAR(30),
    Quantity INT,
    UnitPrice INT,
    Supplier VARCHAR(50),
    LastRestocked DATE
);

select * from ProductInventory;            ---view the table---

-- Inserting the initial data--
INSERT INTO ProductInventory VALUES
(1, 'Laptop', 'Electronics', 20, 70000, 'TechMart', '2025-04-20'),
(2, 'Office Chair', 'Furniture', 50, 5000, 'HomeComfort', '2025-04-18'),
(3, 'Smartwatch', 'Electronics', 30, 15000, 'GadgetHub', '2025-04-22'),
(4, 'Desk Lamp', 'Lighting', 80, 1200, 'BrightLife', '2025-04-25'),
(5, 'Wireless Mouse', 'Electronics', 100, 1500, 'GadgetHub', '2025-04-30');

select * from ProductInventory;            ---view the table---

-- A. CRUD Operations--
--1. Insert a new product--
INSERT INTO ProductInventory (ProductID, ProductName, Category, Quantity, UnitPrice, Supplier, LastRestocked)
VALUES (6, 'Gaming Keyboard', 'Electronics', 40, 3500, 'TechMart', '2025-05-01');

--2. Update stock quantity--
UPDATE ProductInventory
SET Quantity = Quantity + 20
WHERE ProductName = 'Desk Lamp';

--3. Delete a discontinued product(Office Chair)--
DELETE FROM ProductInventory
WHERE ProductID = 2;

--4. Read all products sorted by ProductName--
SELECT * FROM ProductInventory
ORDER BY ProductName ASC;

--B. Sorting and Filtering--
--5. Sort by Quantity (descending)--
SELECT * FROM ProductInventory
ORDER BY Quantity DESC;

--6. Filter by Category--
SELECT * FROM ProductInventory
WHERE Category = 'Electronics';

--7.Filter with AND condition--
SELECT * FROM ProductInventory
WHERE Category = 'Electronics' AND Quantity > 20;

--8.Filter with OR condition--
SELECT * FROM ProductInventory
WHERE Category = 'Electronics' OR UnitPrice < 2000;

--C. Aggregation and Grouping--
--9.Total stock value--
SELECT SUM(Quantity * UnitPrice) AS TotalStockValue
FROM ProductInventory;

--10. Average price by category--
SELECT Category, AVG(UnitPrice) AS AveragePrice
FROM ProductInventory
GROUP BY Category;

--11. Count products by supplier (GadgetHub)--
SELECT COUNT(*) AS ProductCount
FROM ProductInventory
WHERE Supplier = 'GadgetHub';

--D.Conditional and Pattern Matching--
--12. Products starting with 'W'--
SELECT * FROM ProductInventory
WHERE ProductName LIKE 'W%';

--13. GadgetHub products with UnitPrice > 10000--
SELECT * FROM ProductInventory
WHERE Supplier = 'GadgetHub' AND UnitPrice > 10000;

--14. UnitPrice between 1000 and 20000--
SELECT * FROM ProductInventory
WHERE UnitPrice BETWEEN 1000 AND 20000;

--E. Advanced Queries--
--15. Top 3 most expensive products--
SELECT TOP 3 * FROM ProductInventory
ORDER BY UnitPrice DESC;

--16. Products restocked in last 10 days (assuming today is 2025-05-10)--
SELECT * FROM ProductInventory
WHERE LastRestocked >= DATEADD(DAY, -10, '2025-05-10');

--17. Total quantity by supplier--
SELECT Supplier, SUM(Quantity) AS TotalQuantity
FROM ProductInventory
GROUP BY Supplier;

--18. Low stock (Quantity < 30)--
SELECT * FROM ProductInventory
WHERE Quantity < 30;

--F. Subqueries--
--19. Supplier with most products--
SELECT TOP 1 Supplier
FROM ProductInventory
GROUP BY Supplier
ORDER BY COUNT(*) DESC;

--20. Product with highest stock value (Quantity × UnitPrice)--
SELECT TOP 1 *
FROM ProductInventory
ORDER BY (Quantity * UnitPrice) DESC;