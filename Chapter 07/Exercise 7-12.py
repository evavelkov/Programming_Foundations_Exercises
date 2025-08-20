# Programming Exercise 7-12: File Line Reader
#
# Task: Write a program that reads a file and displays specific lines based on user input.
#
# Requirements:
# 1. Create a main function that handles file reading and line display
# 2. Get filename from user input
# 3. Read all lines from the specified file
# 4. Display the total number of lines in the file
# 5. Get line number from user input
# 6. Display the specified line
# 7. Implement comprehensive exception handling
#
# Functions:
# - main(): handles file operations, user input, and display
#
# Logic:
# - Use try-except block for error handling
# - Get filename from user input
# - Open specified file for reading
# - Read all lines into a list using readlines()
# - Close the file
# - Display total number of lines
# - Get line number from user input
# - Convert input to integer
# - Display specified line (adjust for 0-based indexing)
#
# File Operations:
# - open(file_name, 'r') - opens file for reading
# - infile.readlines() - reads all lines into list
# - infile.close() - closes the file
#
# List Operations:
# - len(data) - get number of lines
# - data[line_number - 1] - access specific line (1-based to 0-based)
#
# Exception Handling:
# - IOError: 'An error occurred while trying to read the file.'
# - ValueError: 'Invalid input: Enter an integer.'
# - IndexError: 'Invalid line number.'
#
# Output Format:
# - Total lines: 'The file contains [count] line(s).'
# - Specific line: 'Line [number] is:\n [line content]'
#
# Example:
# Enter the name of the file: sample.txt
# The file contains 15 line(s).
# Enter the line number: 3
# Line 3 is:
# This is the third line of the file.
#
# Note: 
# - Program accepts any filename from user
# - Displays total line count before asking for specific line
# - Handles 1-based line numbering (user input) vs 0-based indexing
# - Implements comprehensive error handling for file and input errors
