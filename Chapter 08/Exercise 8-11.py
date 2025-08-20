# Programming Exercise 8-11: Word Separator
#
# Task: Write a program that separates camelCase words by inserting spaces.
#
# Requirements:
# 1. Create a main function that handles user input and word separation
# 2. Get a string from user input (assumed to be camelCase)
# 3. Insert spaces before uppercase letters (except first character)
# 4. Convert uppercase letters to lowercase (except first character)
# 5. Display the separated words
#
# Functions:
# - main(): handles user input and word separation
#
# Logic:
# - Get string from user input
# - Start result string with first character (unchanged)
# - Use for loop to iterate through remaining characters (index 1 to end)
# - Check if current character is uppercase using isupper()
# - If uppercase:
#   - Convert to lowercase
#   - Add space before the character
# - Add character to result string
# - Display the final result
#
# String Operations:
# - string[0] - get first character
# - for i in range(1, len(string)): - iterate from second character
# - ch.isupper() - check if character is uppercase
# - ch.lower() - convert to lowercase
# - string concatenation with '+'
#
# Example:
# Enter a string: ThisIsACamelCaseString
# This is a camel case string
#
# Note: 
# - Program assumes input is in camelCase format
# - Preserves first character as-is
# - Inserts spaces before uppercase letters
# - Converts uppercase letters to lowercase (except first)
# - Handles any camelCase string
