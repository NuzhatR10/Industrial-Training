# Python Math and Datetime Modules: In-Depth Guide

"""
Author: Kalim Amzad Chy
Email: kalim.amzad.chy@gmail.com

This Python script provides an in-depth guide to the math and datetime modules in Python.
We will explore:
1. Common mathematical functions and constants in the math module.
2. Handling dates and times using the datetime module.
3. Practical examples and real-world applications of both modules.

Each section includes detailed explanations, examples, and assignments.
"""

# Section 1: Math Module
# ----------------------
# The math module provides access to mathematical functions and constants.

import math

# Example 1: Using math functions
print("The square root of 16 is:", math.sqrt(16))
print("Pi is:", math.pi)
print("Euler's number is:", math.e)
print("Cosine of pi is:", math.cos(math.pi))

# Example 2: Using math to solve real-world problems
# Calculate the area of a circle with a given radius
radius = 5
area = math.pi * math.pow(radius, 2)
print(f"The area of the circle is: {area:.2f}")

# Section 2: Datetime Module
# --------------------------
# The datetime module allows you to manipulate dates and times.

import datetime

# Example 3: Working with datetime
now = datetime.datetime.now()
print("Current date and time:", now)
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)


# Example 4: Calculating differences in time
new_year = datetime.datetime(2024, 1, 1)
time_left_for_new_year = new_year - now
print("Days until new year:", time_left_for_new_year.days)

# Example 5: Formatting dates and times
formatted_date = now.strftime("%Y/%m/%d %H:%M:%S")
print("Formatted date and time:", formatted_date)

# Section 3: Practical Applications
# ---------------------------------
# Combining math and datetime for advanced calculations and data handling.

# Example 6: Calculating age in years
def calculate_age(birthdate):
    today = datetime.date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

birthdate = datetime.date(1999, 6, 15)
age = calculate_age(birthdate)
print(f"Age is: {age} years")

# Assignments
# -----------
# Assignment 1: Write a function that calculates compound interest using the formula A = P(1 + r/n)^(nt).
#code:

import math

def calculate_compound_interest(principal, rate, times_compounded, time):
    """
    Calculates compound interest.

    Parameters:
        principal (float): The principal amount (initial investment).
        rate (float): Annual interest rate in percentage (e.g., 5 for 5%).
        times_compounded (int): Number of times interest is compounded per year.
        time (float): Time in years.

    Returns:
        float: Final amount after compound interest.
    """
    # Convert rate from percentage to decimal
    r = rate / 100
    
    # Apply the compound interest formula
    A = principal * math.pow((1 + r / times_compounded), times_compounded * time)
    
    return A


# Example Usage with User Input
if __name__ == "__main__":
    try:
        # Take user inputs
        principal = float(input("Enter the principal amount (initial investment): $"))
        annual_rate = float(input("Enter the annual interest rate (in %): "))
        times_per_year = int(input("Enter the number of times interest is compounded per year: "))
        years = float(input("Enter the investment period in years: "))
        
        # Validate input
        if principal < 0 or annual_rate < 0 or times_per_year <= 0 or years < 0:
            print("Error: Please enter positive values for all inputs.")
        else:
            # Calculate compound interest
            final_amount = calculate_compound_interest(principal, annual_rate, times_per_year, years)
            
            # Display the result
            print("\n--- Compound Interest Calculation ---")
            print(f"Principal Amount: ${principal:.2f}")
            print(f"Annual Interest Rate: {annual_rate}%")
            print(f"Times Compounded Per Year: {times_per_year}")
            print(f"Investment Period: {years} years")
            print(f"Final Amount after Compound Interest: ${final_amount:.2f}")
    except ValueError:
        print("Error: Invalid input. Please enter numerical values.")



# Assignment 2: Create a script that prints the current time and updates every second.

#Code:

import datetime
import time

def display_current_time():
    """
    Displays the current time and updates it every second.
    """
    try:
        print("Press Ctrl+C to stop the program.\n")
        while True:
            # Get the current time
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            
            # Print the current time
            print(f"\rCurrent Time: {current_time}", end="", flush=True)
            
            # Wait for 1 second before updating
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nProgram stopped. Thank you!")

# Run the script
if __name__ == "__main__":
    display_current_time()



# Congratulations on completing the in-depth section on Python's math and datetime modules!
# Review the assignments, try to solve them, and check your understanding of these powerful tools.
