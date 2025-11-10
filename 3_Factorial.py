# Write Python program that uses a recursive function to compute the factorial of a
#  given non-negative integer

# Recursive function to find factorial

def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive call
        return n * factorial(n - 1)

# Input from user
num = int(input("Enter a non-negative integer: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}")
