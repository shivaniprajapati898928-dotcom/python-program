# Given a CSV file containing a single column of integers, write a program to count how many numbers are odd.

import csv

# Input CSV file name
input_file = "numbers.csv"

try:
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        
        odd_count = 0  # counter for odd numbers
        
        # Read each row from the CSV
        for row in reader:
            if row:  # make sure the row is not empty
                num = int(row[0])  # first (and only) column
                if num % 2 != 0:
                    odd_count += 1

    print(f"Total number of odd integers in '{input_file}': {odd_count}")

except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
except ValueError:
    print("Error: The file must contain only integers.")
