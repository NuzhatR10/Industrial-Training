# Python Functions: Comprehensive Guide

"""
Author: Kalim Amzad Chy
Email: kalim.amzad.chy@gmail.com

This Python script provides a comprehensive guide to functions in Python.
We will explore:
1. Basic function definitions and calls.
2. Parameters, arguments, and return values.
3. Variable scope and lifetime within functions.
4. Advanced function concepts like decorators, lambda functions, and error handling.

Each section includes detailed explanations, examples, and assignments.
"""

# Section 1: Basic Functions
# --------------------------
# Functions are defined using the `def` keyword. They allow you to encapsulate code for reuse.

# Example 1: Simple Function
def greet(name: str, age: int = 30):
    """Greets a person with their name."""
    print(f"Hello, {name}! Age: {age}")

greet("Alice")

# Section 2: Parameters and Return Values
# ---------------------------------------
# Functions can accept parameters and return values to the caller.

# Example 2: Function with Parameters and Return Value
def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b

result = add_numbers(5, 3)
# print(f"The sum is {result}.")


# Functions can return multiple values using tuples.
# Example 3: Function with Multiple Return Values
def get_user_data():
    """Returns multiple pieces of user data."""
    name = "Alice"
    age = 30
    membership = True
    return name, age, membership

user_name, user_age, is_member = get_user_data()
print(f"Name: {user_name}, Age: {user_age}, Membership: {is_member}")


# Functions can have default parameters and accept variable numbers of arguments.
# Example 4: Default Arguments and *args, **kwargs
def create_profile(name, email, *interests, **details):
    """Creates a user profile dictionary with given details."""
    profile = {
        "name": name,
        "email": email,
        "interests": interests,
        "details": details
    }
    # process profile

    return profile

profile = create_profile("Bob", "bob@example.com", "nasheed", "art", age=25, location="New York")
print(profile)
profile = create_profile("Bob", "bob@example.com", "nasheed", "art", "calliography", age=35)
print(profile)
profile = create_profile("Bob", "bob@example.com", "swimming", "art", "calliography", "listening_quran", age=27, location="Chicago")
print(profile)


# Section 3: Variable Scope
# -------------------------
# Variables defined inside a function are local to that function. Variables defined outside are global.

# Example 3: Local vs. Global Variables
x = "global"

def test_scope():
    y = "local"
    print("Inside function:", y)

test_scope()
print("Outside function:", x)

# Section 4: Advanced Function Concepts
# -------------------------------------

# Decorators enhance the behavior of functions, and lambda functions allow for concise function definitions.

# Example 3: Using Decorators for Logging
def log_function_data(func):
    """Decorator to log function usage."""
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} was called with args: {args} and kwargs: {kwargs}")
        # save into database with args & kwargs
        return func(*args, **kwargs)
    return wrapper

@log_function_data
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

print(add(10, 5))


# Example 5: Lambda Functions
# Lambda functions are useful for short, simple functions.
# Lambda functions are small anonymous functions defined with the `lambda` keyword.
square = lambda x: x * x
print(f"Square of 5 is {square(5)}.")


# Proper error handling in functions is crucial for robust applications.
# Example 6: Error Handling in Functions
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Only numbers are allowed.")
    except Exception as e:
        print(f"Error: {e}")
    else:
        print(f"The result is {result}")
    finally:
        print("Executing finally clause.")

divide(10, 2)
divide(10, 0)

# Assignments
# -----------
# Assignment 1: Write a function that calculates the factorial of a number and handles any potential errors.


# Function to calculate factorial
def factorial(n: int) -> int:
    """
    Calculates the factorial of a number using recursion.
    
    Parameters:
        n (int): The number to calculate the factorial for.
        
    Returns:
        int: Factorial of the given number.
        
    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    # Error handling for invalid inputs
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    # Base case: Factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    
    # Recursive calculation
    return n * factorial(n - 1)


# Function to safely calculate factorial with error handling
def safe_factorial_calculation():
    """
    Prompts the user for input and calculates the factorial safely,
    handling any errors gracefully.
    """
    try:
        # User input
        user_input = input("Enter a number to calculate its factorial: ")
        number = int(user_input)  # Convert input to integer
        
        # Call the factorial function
        result = factorial(number)
        
        # Print the result
        print(f"The factorial of {number} is: {result}")
        
    except ValueError as ve:
        print(f"Error: {ve}")
    except TypeError as te:
        print(f"Error: {te}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the factorial calculator!")


# Run the program
if __name__ == "__main__":
    safe_factorial_calculation()


# Congratulations on completing the advanced section on Python functions!
# Review the assignments, try to solve them, and check your understanding of function concepts.
