# Python File I/O and JSON Handling: Comprehensive Guide

"""
Author: Kalim Amzad Chy
Email: kalim.amzad.chy@gmail.com

This Python script provides a comprehensive guide to file input/output operations and JSON handling.
We will explore:
1. Reading and writing to plain text files.
2. Working with CSV files using the csv module.
3. Handling JSON data with the json module.
4. Practical examples and real-world applications.

Each section includes detailed explanations, examples, and assignments.
"""

# Section 1: Plain Text Files
# ---------------------------
# Reading and writing plain text files is often the first step in file manipulation.

# Example 1: Writing to a Text File
with open('data/example.txt', 'w') as file:
    file.write("Hello, Python developers!\n")
    file.write("Welcome to file I/O operations.")

# Example 2: Reading from a Text File
with open('data/example.txt', 'r') as file:
    content = file.read() # readlines(), readlines()
    print(content)

# Section 2: CSV Files
# --------------------
# CSV (Comma-Separated Values) files are commonly used for storing tabular data.

import csv

# Example 3: Writing to a CSV File
with open('data/example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 28, "New York"])
    writer.writerow(["Bob", 22, "Los Angeles"])
    writer.writerow(["Carol", 24, "Chicago"])

# Example 4: Reading from a CSV File
with open('data/example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# Section 3: JSON Data
# --------------------
# JSON (JavaScript Object Notation) is a lightweight data-interchange format.

import json

# Example 5: Writing JSON to a File
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
with open('data/data.json', 'w') as file:
    json.dump(data, file)


# Example 6: Reading JSON from a File
with open('data/data.json', 'r') as file:
    data = json.load(file)
    print(data)

# Section 4: Practical Applications
# ---------------------------------
# Combining file I/O with real-world data processing.

# Example 7: Processing JSON Data from a File
# Suppose we have a JSON file containing multiple user records.
users = [
    {"name": "Alice", "age": 25, "email": "alice@example.com"},
    {"name": "Bob", "age": 30, "email": "bob@example.com"}
]
with open('data/users.json', 'w') as file:
    json.dump(users, file)

with open('data/users.json', 'r') as file:
    users = json.load(file)
    for user in users:
        print(f"{user['name']} ({user['age']}): {user['email']}")

# Assignments
# -----------
# Assignment 1: Write a script that reads a CSV file containing product information and converts it into a JSON file.

import csv
import json

# File paths
csv_file_path = 'data/products.csv'
json_file_path = 'data/products.json'

# Read from CSV and convert to JSON
def csv_to_json(csv_file, json_file):
    """
    Reads a CSV file and writes the content to a JSON file.
    """
    try:
        products = []  # List to store product dictionaries

        # Read the CSV file
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)  # Use DictReader for column mapping
            for row in reader:
                products.append(row)  # Append each row as a dictionary

        # Write to JSON file
        with open(json_file, 'w') as file:
            json.dump(products, file, indent=4)  # Save JSON with indentation

        print(f"CSV data successfully converted to JSON and saved at: {json_file}")

    except FileNotFoundError:
        print("Error: The specified CSV file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
if __name__ == "__main__":
    csv_to_json(csv_file_path, json_file_path)


# Assignment 2: Create a log file writer that appends log messages to a file with timestamps.

from datetime import datetime

# File path for the log file
log_file_path = 'data/logs.txt'

def write_log(message, log_file):
    """
    Appends a log message to the log file with a timestamp.
    """
    try:
        # Get the current timestamp
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{current_time}] {message}\n"

        # Append the log entry to the file
        with open(log_file, 'a') as file:
            file.write(log_entry)
        
        print(f"Log message appended: {log_entry.strip()}")

    except Exception as e:
        print(f"An error occurred while writing to the log file: {e}")

# Test the log writer
if __name__ == "__main__":
    write_log("Application started.", log_file_path)
    write_log("Processing data...", log_file_path)
    write_log("Application completed successfully.", log_file_path)


# Congratulations on completing the comprehensive section on Python file I/O and JSON handling!
# Review the assignments, try to solve them, and check your understanding of file operations and data formats.
