# Programming Exercise 6-5: File Number Sum Calculator
#
# Task: Write a program that reads numbers from a file and calculates their sum.
#
# Requirements:
# 1. Create a main function that handles file operations and calculations
# 2. Open 'numbers.txt' file for reading
# 3. Read each line as a number
# 4. Convert each line to a float
# 5. Calculate the total sum of all numbers
# 6. Display the total
#
# Functions:
# - main(): handles file operations, calculations, and display
#
# Logic:
# - Declare variables for total and individual number
# - Use with statement to open 'numbers.txt' file
# - Use for loop to iterate through each line in file
# - Convert each line to float
# - Add each number to running total
# - Display final total using f-string
#
# File Operations:
# - with open('numbers.txt', 'r') as infile: - opens file with automatic closing
# - for line in infile: - iterates through file lines
# - float(line) - converts string to float
#
# Output Format:
# - Use f-string: f'Total: {total}'
#
# Example:
# Total: 45.7
#
# Note: 
# - Program assumes 'numbers.txt' contains one number per line
# - Uses with statement for automatic file closing
# - Handles decimal numbers (float conversion)
