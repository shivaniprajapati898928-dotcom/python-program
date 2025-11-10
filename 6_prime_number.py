# . Create a user-defined module named math_utils with functions for prime checking, factorial, and Fibonacci generation. Import and use it in another program.

# math_utils.py
# A user-defined module with mathematical functions

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Function to compute factorial (recursive)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Function to generate Fibonacci series up to n terms
def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series
