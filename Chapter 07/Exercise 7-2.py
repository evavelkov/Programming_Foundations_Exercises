# Programming Exercise 7-2: Random Number Generator and Display
#
# Task: Write a program that generates random numbers and displays them in a formatted list.
#
# Requirements:
# 1. Import the random module
# 2. Create a main function that generates and displays random numbers
# 3. Initialize a list with 7 zeros
# 4. Generate random numbers between 0 and 9 for each position
# 5. Display the numbers in a single line with comma separators
#
# Functions:
# - main(): handles random number generation and display
#
# Logic:
# - Initialize a list with 7 zeros: [0, 0, 0, 0, 0, 0, 0]
# - Use a for loop to iterate through list indices (0-6)
# - Generate random number between 0 and 9 for each position
# - Assign random number to list at current index
# - Use another for loop to display all numbers
# - Print each number without newline (end='')
# - Add comma and space separator between numbers (except last)
#
# Random Generation:
# - random.randint(0, 9) - generates random integer between 0 and 9
#
# Display Format:
# - Numbers displayed in single line
# - Comma and space separators between numbers
# - No separator after last number
#
# Example:
# 3, 7, 1, 9, 4, 2, 8
#
# Note: 
# - Program generates 7 random single-digit numbers
# - Uses list indexing to assign and access values
# - Controls output formatting with end='' parameter
# - Handles comma separators with conditional logic
