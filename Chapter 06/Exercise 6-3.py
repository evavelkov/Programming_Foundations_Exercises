# Programming Exercise 6-3: File Reading - Line Numbers
#
# Task: Write a program that reads a file and displays each line with its line number.
#
# Requirements:
# 1. Create a main function that handles file operations
# 2. Ask the user to enter a filename
# 3. Open the specified file for reading
# 4. Read all lines and display with line numbers
# 5. Use a for loop to iterate through file lines
# 6. Properly close the file
#
# Functions:
# - main(): handles user input, file operations, and display
#
# Logic:
# - Declare variables for line storage and counter
# - Get filename from user input
# - Open the specified file in read mode
# - Use for loop to iterate through each line in file
# - Increment counter for each line
# - Strip newline characters from each line
# - Display line number and content using f-string
# - Close the file
#
# File Operations:
# - open(fileName, 'r') - opens user-specified file for reading
# - for line in infile: - iterates through file lines
# - line.rstrip('\n') - removes newline character
# - infile.close() - closes the file
#
# Output Format:
# - Use f-string: f'{counter}: {line}'
# - Line numbers start from 1
#
# Example:
# Enter the name of the file: sample.txt
# 1: First line of the file
# 2: Second line of the file
# 3: Third line of the file
#
# Note: Program displays all lines in the file with sequential numbering
