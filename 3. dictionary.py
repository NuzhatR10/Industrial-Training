# Advanced Python: Dictionaries

"""
Author: Kalim Amzad Chy
Email: kalim.amzad.chy@gmail.com

This Python script is designed to provide a comprehensive understanding of Python dictionaries.
We will explore:
1. Dictionary basics - Creation, accessing, and updating.
2. All dictionary methods and their uses.
3. Integrating dictionaries with lists and tuples for complex data structures.

Each section includes detailed explanations, examples, and challenging assignments.
"""

# Section 1: Dictionary Basics
# ----------------------------
# Dictionaries in Python are unordered collections that store data in key-value pairs.

# Example 1: Creating and Using Dictionaries
simple_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(simple_dict["city"])
# print(simple_dict['address'])  # Accessing value by key
print(simple_dict.get('age', 0))  # Accessing value by key
print(simple_dict.get('address', 'Texas'))  # Accessing value by key


# Updating dictionary
simple_dict['age'] = 31  # Updates the age
simple_dict['country'] = 'USA'  # Adds a new key-value pair
# print("Updated Dictionary: ", simple_dict)

# Dictionary Methods
# keys(), values(), items()
print(simple_dict.keys())  # Prints all keys
print(simple_dict.values())  # Prints all values
print(simple_dict.items())  # Prints all key-value pairs as tuples

# get()
print(simple_dict.get('name'))  # Returns 'John'

# pop()
removed_value = simple_dict.pop('country')  # Removes 'country' key and returns its value
print("Removed Value:", removed_value)
print("Dictionary after pop(): ", simple_dict)

# popitem()
last_item = simple_dict.popitem()  # Removes and returns the last inserted key-value pair
print("Last Item:", last_item)
print("Dictionary after popitem(): ", simple_dict)

# update()
simple_dict.update({'age': 32, 'email': 'john@example.com'})  # Updates the dictionary
print("Dictionary after update(): ", simple_dict)

# clear()
# simple_dict.clear()  # Empties the dictionary
# print("Dictionary after clear(): ", simple_dict)

# copy()
dict_copy = simple_dict.copy()  # Creates a shallow copy of the dictionary
print("Dictionary Copy: ", dict_copy)

 #Assignment 1: Create a dictionary representing a student with keys like 'name', 'roll_number', 'grades' (a list of subjects and marks).
# Perform various operations like adding, removing, and modifying elements.#
# Write your code below:


# Creating a dictionary representing a student
student = {
    "name": "Alice",
    "roll_number": 101,
    "grades": {"Math": 85, "Science": 90, "English": 78}
}

# Displaying the original dictionary
print("Original Student Dictionary:", student)

# Adding a new key-value pair
student["age"] = 20
print("After Adding Age:", student)

# Modifying an existing value
student["grades"]["Math"] = 95  # Updating Math grade
print("After Modifying Math Grade:", student)

# Removing a key-value pair
removed_grade = student["grades"].pop("English")  # Removes English grade
print("Removed English Grade:", removed_grade)
print("After Removing English Grade:", student)

# Using update() to add multiple elements
student.update({"city": "New York", "email": "alice@example.com"})
print("After Adding City and Email:", student)

# Using popitem() to remove the last key-value pair
last_item = student.popitem()
print("Removed Last Item:", last_item)
print("After popitem():", student)

# Copying the dictionary
student_copy = student.copy()
print("Copied Dictionary:", student_copy)

# Clearing the dictionary
student.clear()
print("After Clearing Dictionary:", student)







# Section 2: Integrating Dictionaries with Lists and Tuples
# ---------------------------------------------------------
# Dictionaries can be used with lists and tuples to create complex data structures.

# Example 2: List of Dictionaries
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 90},
    {'name': 'Charlie', 'grade': 78}
]

# Sorting list of dictionaries by grade
students_sorted_by_grade = sorted(students, key=lambda x: x['grade'], reverse=True)
print("Students sorted by grade: ", students_sorted_by_grade)

# Example 3: Dictionary of Tuples
# Using tuples as keys
coordinates_info = {(35.6895, 139.6917): "Tokyo", (40.7128, -74.0060): "New York"}

# Assignment 2: Create a dictionary where keys are student names and values are lists of grades. Calculate the average grade for each student.
# Write your code below:

# Creating a dictionary where keys are student names and values are lists of grades
student_grades = {
    "Alice": [85, 90, 78],
    "Bob": [88, 92, 84],
    "Charlie": [70, 75, 80],
    "David": [95, 88, 91]
}

# Calculating the average grade for each student
average_grades = {name: sum(grades) / len(grades) for name, grades in student_grades.items()}

# Displaying the average grades
print("Average Grades for Each Student:")
for name, avg_grade in average_grades.items():
    print(f"{name}: {avg_grade:.2f}")



# Congratulations on completing the advanced section on Python dictionaries!
# Review the assignments, try to solve them, and check your understanding of this powerful data structure.