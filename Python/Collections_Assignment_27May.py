#Lists
#1. List of Squares
for i in range(1,21):
    squares = i ** 2
    print(squares)

#2.Second Largest Number
list1 = [10, 20, 4, 45, 99, 99]

largest = list1[0]
second = None

for num in list1[1:]:
    if num > largest:
        second = largest
        largest = num
    elif num != largest and (second is None or num > second):
        second = num

if second is not None:
    print("Second largest number is:", second)
else:
    print("Second largest number not found.")

#3. Remove Duplicates
list1 = [1, 2, 2, 3, 4, 3, 5, 1, 6]
unique_list = []

for item in list1:
    if item not in unique_list:
        unique_list.append(item)

print("List after removing duplicates:", unique_list)

#4.Rotate List
list1 = [1, 2, 3, 4, 5]
k = 2

k = k % len(list1)

rotated_list = list1[-k:] + list1[:-k]

print("Rotated list:", rotated_list)

#5.List Compression
list1 = [1, 2, 3, 4, 5, 6]
new_list = []
for item in list1:
    if item%2 == 0:
        new_list.append(item*2)
print("New list:", new_list)

#Tuples
#6.Swap Values
def swap_tuples(t1, t2):
    return t2, t1

a, b = (1, 2), (3, 4)
a, b = swap_tuples(a, b)
print("a:", a, "b:", b)

#7.Unpack Tuples
student = ("Simantini", 22, "AIML", "A")
name, age, branch, grade = student
print(f"{name} is {age} years old, studies {branch}, and scored grade {grade}.")

#8.Tuple to Dictionary
t = (("Sim", 1), ("Sam", 2))
d = dict(t)
print(d)

#Sets
#9.Common Items
list1 = input("Enter elements of list1: ").split()
list2 = input("Enter elements of list2: ").split()

set1 = set(list1)
set2 = set(list2)

common_elements = set1.intersection(set2)
print(list(common_elements))

#10.Unique Words in Sentence
sentence = input("Enter sentence: ")
unique_words = set(sentence.split())
print(unique_words)

#11.Symmetric Difference
a = {1, 2, 3}
b = {3, 4, 5}
symmetric_diff = a ^ b
print(symmetric_diff)

#12.Subset Checker
a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))

#Dictionaries
#13.Frequency Counter
string = input("Enter a string: ")
frequency = {}

for char in string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character frequency:")
for char, count in frequency.items():
    print(f"'{char}': {count}")

#14.Student Grade Book
grade = {}
for _ in range(3):
    name = input("Enter student name: ")
    marks = int(input(f"Enter marks for {name}: "))
    grade[name] = marks

# Ask for a student's name to display their grade
student_name = input("Enter the name of the student to get the grade: ")

if student_name in grade:
    marks = grade[student_name]
    if marks >= 90:
        grade = 'A'
    elif marks >= 75:
        grade = 'B'
    else:
        grade = 'C'
    print(f"{student_name}'s grade is: {grade}")
else:
    print("Student not found.")

#15.Merge Two Dictionaries
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}

merged_dict = dict1.copy()

for key, value in dict2.items():
    if key in merged_dict:
        merged_dict[key] += value
    else:
        merged_dict[key] = value

print("Merged dictionary:", merged_dict)

#16.Inverted Dictionary
original_dict = {"a": 1, "b": 2}
inverted_dict = {}

for key, value in original_dict.items():
    inverted_dict[value] = key

print("Inverted dictionary:", inverted_dict)

#17.Group Words by Length
words = input("Enter words separated by space: ").split()

grouped = {}

for word in words:
    length = len(word)
    if length not in grouped:
        grouped[length] = []
    grouped[length].append(word)

print("Words grouped by length:")
for length, word_list in grouped.items():
    print(f"{length}: {word_list}")








