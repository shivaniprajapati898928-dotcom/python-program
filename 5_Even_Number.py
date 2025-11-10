# Write a Python program using map(), filter(), and reduce() to find the sum of squares of even numbers.

from functools import reduce

# Accept list of integers from user
numbers = list(map(int, input("Enter integers separated by spaces: ").split()))

# Step 1: Filter even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Step 2: Square each even number
squares = list(map(lambda x: x ** 2, even_numbers))

# Step 3: Find the sum of squares using reduce
sum_of_squares = reduce(lambda a, b: a + b, squares, 0)

# Display results
print("\nOriginal List:", numbers)
print("Even Numbers:", even_numbers)
print("Squares of Even Numbers:", squares)
print("Sum of Squares of Even Numbers:", sum_of_squares)
