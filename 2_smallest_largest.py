#  Write a Python program to accept a list of integers and perform the following:
    #  • Remove duplicates
    #  • Sort in ascending and descending order
    #  • Display the second largest and smallest element



# Program to process a list of integers

# Accept list of integers from the user
numbers = list(map(int, input("Enter integers separated by spaces: ").split()))

# Remove duplicates using set and convert back to list
unique_numbers = list(set(numbers))

# Sort in ascending order
ascending = sorted(unique_numbers)

# Sort in descending order
descending = sorted(unique_numbers, reverse=True)

print("\nOriginal List:", numbers)
print("After Removing Duplicates:", unique_numbers)
print("Ascending Order:", ascending)
print("Descending Order:", descending)

# Display the second smallest and second largest elements
if len(ascending) >= 2:
    print("Second Smallest Element:", ascending[1])
    print("Second Largest Element:", ascending[-2])
else:
    print("Not enough elements to find second largest and smallest.")
