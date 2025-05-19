USE LibraryDB;

-- Create the Book table--
CREATE TABLE Book (
    BookID INT PRIMARY KEY,
    Title VARCHAR(255),
    Author VARCHAR(255),
    Genre VARCHAR(100),
    Price INT,
    PublishedYear INT,
    Stock INT);

--Insert initial book records--
INSERT INTO Book (BookID, Title, Author, Genre, Price, PublishedYear, Stock) VALUES
(1, 'The Alchemist', 'Paulo Coelho', 'Fiction', 300, 1988, 50),
(2, 'Sapiens', 'Yuval Noah Harari', 'Non-Fiction', 500, 2011, 30),
(3, 'Atomic Habits', 'James Clear', 'Self-Help', 400, 2018, 25),
(4, 'Rich Dad Poor Dad', 'Robert Kiyosaki', 'Personal Finance', 350, 1997, 20),
(5, 'The Lean Startup', 'Eric Ries', 'Business', 450, 2011, 15);

-- 1. CRUD Operations--
-- 1.1 Add new book--
INSERT INTO Book (BookID, Title, Author, Genre, Price, PublishedYear, Stock)
VALUES (6, 'Deep Work', 'Cal Newport', 'Self-Help', 420, 2016, 35);

-- 1.2 Update Self-Help book prices (+50)--
UPDATE Book
SET Price = Price + 50
WHERE Genre = 'Self-Help';

-- 1.3 Delete book with BookID = 4--
DELETE FROM Book
WHERE BookID = 4;

-- 1.4 Read all books sorted by Title--
SELECT * FROM Book
ORDER BY Title ASC;

-- 2. Sorting and Filtering--
-- 2.1 Sort by price descending--
SELECT * FROM Book
ORDER BY Price DESC;

-- 2.2 Filter by genre = Fiction--
SELECT * FROM Book
WHERE Genre = 'Fiction';

-- 2.3 Self-Help books priced above 400--
SELECT * FROM Book
WHERE Genre = 'Self-Help' AND Price > 400;

-- 2.4 Fiction OR published after 2000--
SELECT * FROM Book
WHERE Genre = 'Fiction' OR PublishedYear > 2000;

-- 3. Aggregation and Grouping--
-- 3.1 Total stock value (Price × Stock)--
SELECT SUM(Price * Stock) AS TotalStockValue FROM Book;

-- 3.2 Average price by genre--
SELECT Genre, AVG(Price) AS AvgPrice
FROM Book
GROUP BY Genre;

-- 3.3 Total books by Paulo Coelho--
SELECT COUNT(*) AS BookCount
FROM Book
WHERE Author = 'Paulo Coelho';

--4. Conditional and Pattern Matching--
-- 4.1 Titles containing "The"--
SELECT * FROM Book
WHERE Title LIKE '%The%';

-- 4.2 Books by Yuval Noah Harari priced below 600--
SELECT * FROM Book
WHERE Author = 'Yuval Noah Harari' AND Price < 600;

-- 4.3 Books priced between 300 and 500--
SELECT * FROM Book
WHERE Price BETWEEN 300 AND 500;

--5. Advanced Queries--
-- 5.1 Top 3 most expensive books--
SELECT TOP 3 *
FROM Book
ORDER BY Price DESC;

-- 5.2 Books published before 2000--
SELECT * FROM Book
WHERE PublishedYear < 2000;

-- 5.3 Total number of books in each genre--
SELECT Genre, COUNT(*) AS BookCount
FROM Book
GROUP BY Genre;

-- 5.4 Duplicate titles--
SELECT Title, COUNT(*) AS Count
FROM Book
GROUP BY Title
HAVING COUNT(*) > 1;

--6. Join and Subqueries--
-- 6.1 Author with the most books--
SELECT TOP 1 Author, COUNT(*) AS BookCount
FROM Book
GROUP BY Author
ORDER BY BookCount DESC;

-- 6.2 Oldest book by genre--
WITH OldestBooks AS (
    SELECT Genre, MIN(PublishedYear) AS OldestYear
    FROM Book
    GROUP BY Genre
)
SELECT b.Genre, b.Title, b.Author, b.PublishedYear
FROM Book b
JOIN OldestBooks ob ON b.Genre = ob.Genre AND b.PublishedYear = ob.OldestYear;