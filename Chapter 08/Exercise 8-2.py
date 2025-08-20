# Programming Exercise 8-2: String Digit Sum Calculator
#
# Task: Write a program that calculates the sum of all digits in a string.
#
# Requirements:
# 1. Create a main function that handles user input and calls calculation function
# 2. Create a string_total function that calculates sum of digits in a string
# 3. Get a string of digits from user input (no separators)
# 4. Calculate the total of all digits in the string
# 5. Display the result
#
# Functions:
# - main(): handles user input and displays results
# - string_total(string): calculates sum of digits in string
#
# Logic:
# - Get string of digits from user input
# - Call string_total function with the string
# - Display the total
# - In string_total function:
#   - Initialize total to 0
#   - Use for loop to iterate through each character in string
#   - Convert each character to integer using int()
#   - Add each digit to running total
#   - Return the total
#
# String Operations:
# - len(string) - get string length
# - string[i] - access character at index i
# - int(char) - convert character to integer
#
# Example:
# Enter a sequence of digits with nothing separating them: 12345
# The total of the digits in the string you entered is 15
#
# Note: 
# - Program assumes string contains only digit characters
# - Uses string indexing to access each character
# - Converts each character to integer for calculation
# - Handles strings of any length
