# Write a Python program that takes user input for two numbers and performs division.  Handle exceptions for invalid input, divide by zero, and unexpected errors gracefully. 

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = a / b
    print(f"Result: {result}")
except ValueError:
    print("Error: Please enter valid numeric values.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print("Unexpected error:", e)

