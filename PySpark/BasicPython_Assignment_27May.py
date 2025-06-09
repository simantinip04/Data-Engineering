#Variables, Data Types and Operators
# 1. Digit sum Calculator
num = int(input("Enter a number: "))
sum = 0
for digit in str(num):
    sum += int(digit)
print(sum)

#2. Reverse a 3-digit no
num = int(input("Enter a 3-digit number: "))
if 100<=num<=999:
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num *= 10 +digit
        num //= 10
    print("Reversed No:", reversed_num)
else:
    print("Invalid input")

#3. Unit Convertor(m to cm,ft,in)
dist = float(input("Enter distance in meters: "))
print("Distance in meter:", dist)
dist_in_cm = dist * 100
print("Distance in cm:",dist_in_cm)
dist_in_ft = dist * 3.28084
print("Distance in ft:",dist_in_ft)
dist_in_inc = dist * 39.3701
print("Distance in inches:",dist_in_inc)

#4.Percentage Calculator
print("Enter Marks out of 100 for each subject")
sub1=int(input("Enter Marks for Subject 1: "))
sub2=int(input("Enter Marks for Subject 2: "))
sub3=int(input("Enter Marks for Subject 3: "))
sub4=int(input("Enter Marks for Subject 4: "))
sub5=int(input("Enter Marks for Subject 5: "))

total_of_marks = sub1 + sub2 + sub3 + sub4 + sub5
average_marks = total_of_marks / 5
percentage=(total_of_marks/500)*100

print("\n---Result---")
print("Total Marks Obtained in 5 Subjects:", total_of_marks)
print("Average Marks Obtained in 5 Subjects:", average_marks)
print("Percentage obtained:", percentage, "%")

if percentage >= 90:
    print("Grade is A")
elif 80 <= percentage < 90:
    print("Grade is B")
elif 70 <= percentage < 80:
    print("Grade is C")
elif 40 <= percentage < 70:
    print("Grade is D")
else:
    print("Grade is Fail")

#Conditionals
#5. Leap Year Check
year = int(input("Enter year: "))
if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print(year,"is a Leap Year")
else:
    print(year,"is not a Leap Year")

#6.Simple Calculator
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

operator = input("Enter operator(+, -, *, /): ")

if operator == "+":
    result = num1 + num2
    print("Addition is:",result)
elif operator == "-":
    result = num1 - num2
    print("Subtraction is:",result)
elif operator == "*":
    result = num1 * num2
    print("Multiplication is:",result)
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("Division is:",result)
    else:
        print("Division by 0 not allowed")
else:
    print("Invalid operator")

#7. Triangle Validator
side1=float(input("Enter side1: "))
side2=float(input("Enter side2: "))
side3=float(input("Enter side3: "))

if side1+side2>side3 and side2+side3>side1 and side1+side3>side2:
    print("Given sides can form a triangle")
else:
    print("Given sides cannot form a triangle")

#8.Bill Splitter with Tip
total_bill_amt = float(input("Enter Total Bill Amount: "))
no_of_people = int(input("Enter Number of People: "))
tip_percentage = float(input("Enter Tip Percentage: "))

tip_amt = (tip_percentage /100) * total_bill_amt

total_bill = total_bill_amt + tip_amt

amt_per_person= total_bill/no_of_people
print("Amount per person:", round(amt_per_person,2))

#LOOPS
#9.Find All Prime Numbers Between 1 and 100
print("Prime numbers between 1 and 100 are:")

for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")

#10.Palindrome Checker
string = input("Enter a word:")
string = string.replace(" ","").lower()
is_palindrome = True
for i in range(len(string)//2):
    if string[i] != string[-i-1]:
        is_palindrome = False
        break
if is_palindrome:
    print(string, "is a Palindrome")
else:
    print(string, "is not a Palindrome")

#11. Fibonacci Series
num = int(input("Enter the number of terms: "))

a, b = 0, 1

print("Fibonacci Series:")

for i in range(num):
    print(a, end=" ")
    a, b = b, a + b

#12. Multiplication Table (User Input)
num = int(input("Enter the number: "))
print("---Table of",num,"---")
for i in range(1,11):
    print(f"{num} x {i} = {num * i}")

#13.Number Guessing Game
import random
guessing_number = random.randint(1, 100)
print("Guess the number between 1 and 100: ")

while True:
    guess = int(input("Enter your guess: "))

    if guess < guessing_number:
        print("Too Low!")
    elif guess > guessing_number:
        print("Too High!")
    else:
        print("Congratulations! You guessed it right.")
        break

#14. ATM Machine Simulation
balance = 10000

while True:
    print("\n--- ATM Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"Deposited {amount}. New balance: {balance}")
        else:
            print("Invalid amount!")
    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        if 0 < amount <= balance:
            balance -= amount
            print(f"Withdrew {amount}. New balance: {balance}")
        else:
            print("Invalid amount or insufficient balance!")
    elif choice == '3':
        print(f"Current balance: {balance}")
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice! Please select 1-4.")

#15.Password Strength Checker
import string

password = input("Enter a password: ")

has_number = any(char.isdigit() for char in password)
has_upper = any(char.isupper() for char in password)
has_symbol = any(char in string.punctuation for char in password)
length_ok = len(password) >= 8

if length_ok and has_number and has_upper and has_symbol:
    print("Strong password!")
else:
    print("Weak password. Requirements:")
    if not length_ok:
        print("- At least 8 characters")
    if not has_number:
        print("- At least one number")
    if not has_upper:
        print("- At least one uppercase letter")
    if not has_symbol:
        print("- At least one symbol (e.g., !, @, #, etc.)")

#16.Find GCD (Greatest Common Divisor)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    a, b = b, a % b

print("GCD is:", a)








