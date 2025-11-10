# Q1: Fibonacci numbers using for loop and while loop in python

# n = int(input("Enter the number of terms: "))
# a, b = 0, 1

# print("Fibonacci Series:")
# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b



# Fibonacci Series using while loop

n = int(input("Enter the number of terms: "))
a, b = 0, 1
count = 0

print("Fibonacci Series:")
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
