# Write a program that reads a text file and replaces all occurrences of a given word with another word. Save the modified content into a new file.


# Program to replace all occurrences of a word in a text file

# Input and output file names

input_file = "input.txt"
output_file = "modified.txt"

# Ask user for words to replace
old_word = input("Enter the word to be replaced: ")
new_word = input("Enter the new word: ")

try:
    # Read the original file
    with open(input_file, 'r') as f:
        text = f.read()

    # Replace all occurrences of the old word
    modified_text = text.replace(old_word, new_word)

    # Write the modified text to a new file
    with open(output_file, 'w') as f:
        f.write(modified_text)

    print(f"\nAll occurrences of '{old_word}' have been replaced with '{new_word}'.")
    print(f"Modified content has been saved to '{output_file}'.")
except FileNotFoundError:
    print(f"Error: File '{input_file}' not found. Please make sure it exists.")
