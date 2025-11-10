# Write a program that accepts a word from the user and displays all the line numbers in which that word occurs in a text file.

# Program to find line numbers where a word occurs in a text file

# Input file name
input_file = "input.txt"

# Ask user for the word to search
search_word = input("Enter the word to search: ").lower()

try:
    # Open and read the file
    with open(input_file, 'r') as f:
        lines = f.readlines()

    found_lines = []  # list to store line numbers

    # Check each line for the word
    for i, line in enumerate(lines, start=1):
        # Convert line to lowercase for case-insensitive match
        if search_word in line.lower():
            found_lines.append(i)

    # Display results
    if found_lines:
        print(f"\nThe word '{search_word}' occurs in the following line(s): {found_lines}")
    else:
        print(f"\nThe word '{search_word}' was not found in the file.")
except FileNotFoundError:
    print(f"Error: File '{input_file}' not found. Please make sure it exists.")
