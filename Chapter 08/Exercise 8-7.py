# Programming Exercise 8-7: Character Type Counter
#
# Task: Write a program that counts different types of characters in a text file.
#
# Requirements:
# 1. Create a main function that handles file reading and character counting
# 2. Read all content from 'text.txt' file
# 3. Count uppercase letters, lowercase letters, digits, and spaces
# 4. Display the counts for each character type
#
# Functions:
# - main(): handles file operations and character counting
#
# Logic:
# - Open 'text.txt' file using with statement
# - Read entire file content into a string using read()
# - Initialize counters for each character type
# - Use for loop to iterate through each character in file content
# - Check character type using string methods:
#   - ch.isupper() - check if uppercase letter
#   - ch.islower() - check if lowercase letter
#   - ch.isdigit() - check if digit
#   - ch.isspace() - check if space
# - Increment appropriate counter for each character type
# - Display all counts with proper formatting
#
# File Operations:
# - with open('text.txt', 'r') as infile: - opens file for reading
# - infile.read() - reads entire file content
#
# String Methods:
# - ch.isupper() - check if character is uppercase letter
# - ch.islower() - check if character is lowercase letter
# - ch.isdigit() - check if character is digit
# - ch.isspace() - check if character is whitespace
#
# Example:
# Uppercase letters: 45
# Lowercase letters: 234
# Digits: 12
# Spaces: 67
#
# Note: 
# - Program assumes 'text.txt' exists
# - Uses with statement for automatic file closing
# - Counts all character types in the entire file
# - Uses built-in string methods for character classification
