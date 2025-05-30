# Section 1: Python Basics & Control Flow

# Q1. Print all odd numbers between 10 and 50
print("Q1: Odd numbers between 10 and 50:")
for i in range(11, 50, 2):
    print(i, end=" ")
print("\n")

# Q2. Check if a year is a leap year
print("Q2: Leap year checker")
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print("2024 is leap year:", is_leap_year(2024), "\n")

# Q3. Count number of times 'a' appears in a string
print("Q3: Count of letter 'a'")
text = "This is a sample data string."
count = 0
for char in text:
    if char.lower() == 'a':
        count += 1
print("Count of 'a':", count, "\n")

# Section 2: Collections

# Q4. Create dictionary from lists
print("Q4: Create dictionary from lists")
keys = ['a', 'b', 'c']
values = [100, 200, 300]
my_dict = dict(zip(keys, values))
print(my_dict, "\n")

# Q5. Analyze employee salaries
print("Q5: Max, above average, and sorted descending salaries")
salaries = [50000, 60000, 55000, 70000, 52000]
max_salary = max(salaries)
average = sum(salaries) / len(salaries)
above_avg = [s for s in salaries if s > average]
sorted_desc = sorted(salaries, reverse=True)
print("Max:", max_salary)
print("Above Average:", above_avg)
print("Sorted Desc:", sorted_desc, "\n")

# Q6. Set difference
print("Q6: Set difference")
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
set_a = set(a)
set_b = set(b)
print("Set A:", set_a)
print("Set B:", set_b)
print("A - B:", set_a - set_b, "\n")

# Section 3: Functions & Classes

# Q7. Employee class
print("Q7–9: Employee class & high earners")
class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def display(self):
        print(f"{self.name} ({self.emp_id}) - {self.department} - ₹{self.salary}")

    def is_high_earner(self):
        return self.salary > 60000

# Q8. Project class
class Project(Employee):
    def __init__(self, emp_id, name, department, salary, project_name, hours_allocated):
        super().__init__(emp_id, name, department, salary)
        self.project_name = project_name
        self.hours_allocated = hours_allocated

# Q9. Instantiate and check high earners
e1 = Employee(1, "Ali", "HR", 50000)
e2 = Employee(2, "Neha", "IT", 60000)
e3 = Employee(4, "Sara", "IT", 70000)

for e in [e1, e2, e3]:
    e.display()
    print("High Earner:", e.is_high_earner())
print()

# Section 4: File Handling

# Q10. Write IT employees to a file
import csv
print("Q10: Writing IT employees to file")
with open("employees.csv", "r") as file, open("it_employees.txt", "w") as output:
    reader = csv.DictReader(file)
    for row in reader:
        if row['Department'] == 'IT':
            output.write(row['Name'] + "\n")
print("Written to it_employees.txt\n")

# Q11. Count words in file
print("Q11: Count words in a file")
with open("sample.txt", "r") as f:
    text = f.read()
    words = text.split()
    print("Word count:", len(words), "\n")

# Section 5: Exception Handling

# Q12. Square with exception handling
print("Q12: Square a number with exception handling")
try:
    num = int(input("Enter a number: "))
    print("Square:", num ** 2)
except ValueError:
    print("Invalid input!\n")

# Q13. Handle ZeroDivisionError
print("Q13: Handle ZeroDivisionError")
def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Cannot divide by zero."
print("Divide 10 by 0:", divide(10, 0), "\n")

# Section 6: Pandas – Reading & Exploring CSVs

import pandas as pd
from datetime import datetime

print("Q14: Load CSVs")
employees = pd.read_csv("employees.csv")
projects = pd.read_csv("projects.csv")
print("CSV files loaded\n")

# Q15. Display insights
print("Q15: Employee data insights")
print(employees.head(2))
print("Unique departments:", employees['Department'].unique())
print("Average salary by dept:\n", employees.groupby('Department')['Salary'].mean(), "\n")

# Q16. Add TenureInYears
print("Q16: Add TenureInYears column")
employees['JoiningDate'] = pd.to_datetime(employees['JoiningDate'])
employees['TenureInYears'] = datetime.now().year - employees['JoiningDate'].dt.year
print(employees[['Name', 'TenureInYears']], "\n")

# Section 7: Filtering, Aggregation, Sorting

# Q17. Filter IT employees with salary > 60000
print("Q17: IT employees with salary > 60000")
high_paid_it = employees[(employees['Department'] == 'IT') & (employees['Salary'] > 60000)]
print(high_paid_it, "\n")

# Q18. Group by Department
print("Q18: Group by Department")
dept_group = employees.groupby('Department').agg(
    EmployeeCount=('EmployeeID', 'count'),
    TotalSalary=('Salary', 'sum'),
    AverageSalary=('Salary', 'mean')
)
print(dept_group, "\n")

# Q19. Sort by salary descending
print("Q19: Sort by salary (descending)")
sorted_emps = employees.sort_values(by='Salary', ascending=False)
print(sorted_emps, "\n")

# Section 8: Joins & Merging

# Q20. Merge employees and projects
print("Q20: Merged employees and projects")
merged = pd.merge(employees, projects, on='EmployeeID')
print(merged, "\n")

# Q21. Employees not working on any project
print("Q21: Employees with no projects")
left_merged = pd.merge(employees, projects, on='EmployeeID', how='left')
no_projects = left_merged[left_merged['ProjectID'].isna()]
print(no_projects[['EmployeeID', 'Name']], "\n")

# Q22. Add TotalCost = HoursAllocated * (Salary / 160)
print("Q22: Add TotalCost column")
merged['TotalCost'] = merged['HoursAllocated'] * (merged['Salary'] / 160)
print(merged[['EmployeeID', 'Name', 'ProjectName', 'TotalCost']])
