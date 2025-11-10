# Write Python program that uses a recursive function to find the digital sum of a given integer.
# Recursive function to find digital sum

def digital_sum(n):
    # Base case: if the number is a single digit
    if n < 10:
        return n
    else:
        # Recursive case: add last digit to sum of remaining digits
        return (n % 10) + digital_sum(n // 10)

# Input from user
num = int(input("Enter an integer: "))

# Ensure positive integer for calculation
num = abs(num)

# Call the recursive function
result = digital_sum(num)

print(f"The digital sum of {num} is {result}")
