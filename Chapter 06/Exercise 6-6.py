# Programming Exercise 6-6: File Number Average Calculator
#
# Task: Write a program that reads numbers from a file and calculates their average.
#
# Requirements:
# 1. Create a main function that handles file operations and calculations
# 2. Open 'numbers.txt' file for reading
# 3. Read each line as a number
# 4. Convert each line to a float
# 5. Calculate the sum and count of numbers
# 6. Calculate the average (sum / count)
# 7. Display the average
#
# Functions:
# - main(): handles file operations, calculations, and display
#
# Logic:
# - Declare variables for total, individual number, and counter
# - Use with statement to open 'numbers.txt' file
# - Use for loop to iterate through each line in file
# - Increment counter for each number
# - Convert each line to float
# - Add each number to running total
# - Calculate average = total / counter
# - Display final average using f-string
#
# File Operations:
# - with open('numbers.txt', 'r') as infile: - opens file with automatic closing
# - for line in infile: - iterates through file lines
# - float(line) - converts string to float
#
# Calculations:
# - counter = counter + 1 (or counter += 1)
# - total += number
# - average = total / counter
#
# Output Format:
# - Use f-string: f'Average: {average}'
#
# Example:
# Average: 15.23
#
# Note: 
# - Program assumes 'numbers.txt' contains one number per line
# - Uses with statement for automatic file closing
# - Handles decimal numbers (float conversion)
# - Calculates arithmetic mean of all numbers in file
