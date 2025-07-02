use SupplyChainDB;

--Suppliers table
CREATE TABLE Suppliers (
    SupplierID INT IDENTITY(1,1) PRIMARY KEY,
    Name NVARCHAR(100),
    Email NVARCHAR(100),
    PhoneNumber NVARCHAR(20)
);

--Inventory table
CREATE TABLE Inventory (
    ItemID INT IDENTITY(1,1) PRIMARY KEY,
    ItemName NVARCHAR(100),
    StockLevel INT,
    ReorderThreshold INT,
    SupplierID INT FOREIGN KEY REFERENCES Suppliers(SupplierID)
);

--Orders table
CREATE TABLE Orders (
    OrderID INT IDENTITY(1,1) PRIMARY KEY,
    ItemID INT FOREIGN KEY REFERENCES Inventory(ItemID),
    Quantity INT,
    OrderDate DATE,
    ExpectedDelivery DATE
);

select * from Suppliers;
select * from Inventory;
select * from Orders;

---Basic CRUD Operations---
---1.Suppliers Table---
INSERT INTO Suppliers (Name, Email, PhoneNumber) VALUES       ---Create
('Tech Supplies', 'tech@supplies.com', '9876543210'),
('Smart Parts Co', 'info@smartparts.com', '9123456789');

SELECT * FROM Suppliers WHERE Name = 'Tech Supplies';         ---Read

UPDATE Suppliers                                              ---Update
SET PhoneNumber = '9999999999'
WHERE SupplierID = 1;

DELETE FROM Suppliers                                         ---Delete
WHERE SupplierID = 2;

select * from Suppliers;

---2.Inventory Table---
INSERT INTO Inventory (ItemName, StockLevel, ReorderThreshold, SupplierID)VALUES               ---Create
('Laptop Charger', 50, 20, 1),
('SSD Drive', 25, 10, 1);

SELECT * FROM Inventory                              ---Read
WHERE StockLevel < ReorderThreshold;

UPDATE Inventory                                     ---Update
SET StockLevel = 10
WHERE ItemID = 1;

DELETE FROM Inventory                                ---Delete
WHERE ItemID = 2;

select * from Inventory;

---3.Orders Table---
INSERT INTO Orders (ItemID, Quantity, OrderDate, ExpectedDelivery) VALUES            ---Create
(1, 30, GETDATE(), DATEADD(DAY, 7, GETDATE()));

SELECT * FROM Orders                     ---Read
WHERE ItemID = 1;

UPDATE Orders                            ---Update
SET ExpectedDelivery = DATEADD(DAY, 10, GETDATE())
WHERE OrderID = 1;

DELETE FROM Orders                       ---Delete
WHERE OrderID = 1;

select * from Orders;

---Stored procedures (Auto Reorder trigger)---
CREATE TRIGGER trg_AutoReorder
ON Inventory
AFTER UPDATE
AS
BEGIN
    SET NOCOUNT ON;

    -- Insert an order for each item whose stock fell below reorder threshold after update
    INSERT INTO Orders (ItemID, Quantity, OrderDate, ExpectedDelivery)
    SELECT i.ItemID, i.ReorderThreshold, GETDATE(), DATEADD(DAY, 7, GETDATE())
    FROM Inserted i
    WHERE i.StockLevel < i.ReorderThreshold;
END;

