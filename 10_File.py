# Write a program to read a text file and count the frequency of each word, storing the result in another file

# Program to count word frequency in a text file

# Input and output file names
input_file = "input.txt"
output_file = "word_count.txt"

# Read the input file
with open(input_file, 'r') as f:
    text = f.read()

# Convert text to lowercase and split into words
words = text.lower().split()

# Remove punctuation using str.strip()
cleaned_words = [word.strip('.,!?;:"()[]') for word in words]

# Count word frequency
word_count = {}
for word in cleaned_words:
    if word:
        word_count[word] = word_count.get(word, 0) + 1

# Write results to another file
with open(output_file, 'w') as f:
    f.write("Word Frequency Count:\n")
    for word, count in sorted(word_count.items()):
        f.write(f"{word}: {count}\n")

print(f"Word frequency count has been written to '{output_file}'.")
