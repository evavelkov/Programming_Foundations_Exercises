# Programming Exercise 6-9: File Average Calculator with Exception Handling
#
# Task: Write a program that calculates the average of numbers from a file with proper exception handling.
#
# Requirements:
# 1. Create a main function that handles file operations and calculations
# 2. Open 'numbers.txt' file for reading
# 3. Read each line as a number and calculate average
# 4. Implement exception handling for different error types
# 5. Display appropriate error messages for different scenarios
#
# Functions:
# - main(): handles file operations, calculations, and exception handling
#
# Logic:
# - Declare variables for total, individual number, and counter
# - Use try-except block to handle potential errors
# - Use with statement to open 'numbers.txt' file
# - Use for loop to iterate through each line in file
# - Increment counter for each number
# - Convert each line to float
# - Add each number to running total
# - Calculate average = total / counter
# - Display final average using f-string
# - Handle specific exceptions with appropriate messages
#
# Exception Handling:
# - IOError: File cannot be read
# - ValueError: Non-numeric data found in file
# - General exception: Any other error
#
# File Operations:
# - with open('numbers.txt', 'r') as infile: - opens file with automatic closing
# - for line in infile: - iterates through file lines
# - float(line) - converts string to float
#
# Error Messages:
# - IOError: 'An error occurred while trying to read the file.'
# - ValueError: 'Non-numeric data found in the file'
# - General: 'An error occurred'
#
# Example:
# Average: 15.23
# (or appropriate error message if file cannot be read)
#
# Note: 
# - Program assumes 'numbers.txt' contains one number per line
# - Uses with statement for automatic file closing
# - Handles decimal numbers (float conversion)
# - Provides specific error messages for different failure scenarios
