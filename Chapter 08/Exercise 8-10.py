# Programming Exercise 8-10: Most Frequent Character Finder
#
# Task: Write a program that finds the character that appears most frequently in a string.
#
# Requirements:
# 1. Create a main function that handles user input and frequency analysis
# 2. Create arrays to track character frequencies
# 3. Get a string from user input
# 4. Count frequency of each letter (A-Z)
# 5. Find the most frequently occurring letter
# 6. Display the result
#
# Functions:
# - main(): handles user input and frequency analysis
#
# Logic:
# - Create count array with 26 elements (one for each letter A-Z)
# - Create letters string: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# - Get string from user input
# - Use for loop to iterate through each character in string
# - Convert each character to uppercase
# - Find character's position in letters string using find()
# - If character is a letter (index >= 0), increment count array
# - Find position of highest frequency in count array
# - Display the most frequent character
#
# Data Structures:
# - count array: tracks frequency of each letter (A-Z)
# - letters string: contains all uppercase letters
#
# String Operations:
# - for ch in string: - iterate through characters
# - ch.upper() - convert to uppercase
# - letters.find(ch) - find character position in letters string
#
# Array Operations:
# - count[index] += 1 - increment frequency count
# - Find maximum value in count array
#
# Example:
# Enter a string: Mississippi
# The character that appears most frequently in the string is S.
#
# Note: 
# - Program counts only letters (A-Z, case insensitive)
# - Ignores spaces, punctuation, and numbers
# - If multiple characters have same frequency, displays first one
# - Uses array indexing to track character frequencies
