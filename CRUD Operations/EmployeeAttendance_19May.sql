use Employee;

CREATE TABLE EmployeeAttendance (
    AttendanceID INT PRIMARY KEY,
    EmployeeName VARCHAR(100),
    Department VARCHAR(100),
    Date DATE,
    Status VARCHAR(20),
    HoursWorked INT
);

select * from EmployeeAttendance;

-- Insert initial records--
INSERT INTO EmployeeAttendance VALUES
(1, 'John Doe', 'IT', '2025-05-01', 'Present', 8),
(2, 'Priya Singh', 'HR', '2025-05-01', 'Absent', 0),
(3, 'Ali Khan', 'IT', '2025-05-01', 'Present', 7),
(4, 'Riya Patel', 'Sales', '2025-05-01', 'Late', 6),
(5, 'David Brown', 'Marketing', '2025-05-01', 'Present', 8);

select * from EmployeeAttendance;

--1. CRUD Operations--
-- 1. Insert a new attendance record
INSERT INTO EmployeeAttendance VALUES
(6, 'Neha Sharma', 'Finance', '2025-05-01', 'Present', 8);

-- 2. Update Riya Patel's status from Late to Present
UPDATE EmployeeAttendance
SET Status = 'Present'
WHERE EmployeeName = 'Riya Patel' AND Date = '2025-05-01';

-- 3. Delete the record for Priya Singh
DELETE FROM EmployeeAttendance
WHERE EmployeeName = 'Priya Singh' AND Date = '2025-05-01';

-- 4. Display all records sorted by EmployeeName (ascending)
SELECT * FROM EmployeeAttendance
ORDER BY EmployeeName ASC;

--2. Sorting and Filtering--
-- 5. Sort employees by HoursWorked in descending order
SELECT * FROM EmployeeAttendance
ORDER BY HoursWorked DESC;

-- 6. Attendance records for IT department
SELECT * FROM EmployeeAttendance
WHERE Department = 'IT';

-- 7. Present employees from IT department
SELECT * FROM EmployeeAttendance
WHERE Department = 'IT' AND Status = 'Present';

-- 8. Employees who are either Absent or Late
SELECT * FROM EmployeeAttendance
WHERE Status = 'Absent' OR Status = 'Late';

--3. Aggregation and Grouping--
-- 9. Total hours worked grouped by Department
SELECT Department, SUM(HoursWorked) AS TotalHours
FROM EmployeeAttendance
GROUP BY Department;

-- 10. Average hours worked per day across all departments
SELECT AVG(HoursWorked) AS AverageHoursPerDay
FROM EmployeeAttendance;

-- 11. Count of employees by attendance Status
SELECT Status, COUNT(*) AS Count
FROM EmployeeAttendance
GROUP BY Status;

--4. Conditional and Pattern Matching--
-- 12. Employees whose names start with 'R'
SELECT * FROM EmployeeAttendance
WHERE EmployeeName LIKE 'R%';

-- 13. Employees who worked >6 hours and are Present
SELECT * FROM EmployeeAttendance
WHERE HoursWorked > 6 AND Status = 'Present';

-- 14. Employees who worked between 6 and 8 hours
SELECT * FROM EmployeeAttendance
WHERE HoursWorked BETWEEN 6 AND 8;

-- 5. Advanced Queries--
-- 15. Top 2 employees with the most hours worked
SELECT TOP 2 *
FROM EmployeeAttendance
ORDER BY HoursWorked DESC;

-- 16. Employees who worked less than average hours
SELECT * FROM EmployeeAttendance
WHERE HoursWorked < (
    SELECT AVG(HoursWorked) FROM EmployeeAttendance
);

-- 17. Average hours worked by Status
SELECT Status, AVG(HoursWorked) AS AvgHours
FROM EmployeeAttendance
GROUP BY Status;

-- 18. Find duplicate entries (same employee on same date)
SELECT EmployeeName, Date, COUNT(*) AS EntryCount
FROM EmployeeAttendance
GROUP BY EmployeeName, Date
HAVING COUNT(*) > 1;

--7. Join/Subquery Based--
-- 19. Department with the most Present employees
SELECT TOP 1 Department
FROM EmployeeAttendance
WHERE Status = 'Present'
GROUP BY Department
ORDER BY COUNT(*) DESC;

-- 20. Employee with max hours worked in each department
SELECT Department, EmployeeName, HoursWorked
FROM EmployeeAttendance ea1
WHERE HoursWorked = (
    SELECT MAX(HoursWorked)
    FROM EmployeeAttendance ea2
    WHERE ea2.Department = ea1.Department
);
