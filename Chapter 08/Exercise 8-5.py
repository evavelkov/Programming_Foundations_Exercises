# Programming Exercise 8-5: Telephone Number Converter
#
# Task: Write a program that converts alphabetic phone numbers to numeric format.
#
# Requirements:
# 1. Create a main function that handles user input and phone number conversion
# 2. Create a list of digit mappings for letters
# 3. Get alphabetic phone number from user input (XXX-XXX-XXXX format)
# 4. Convert letters to corresponding digits
# 5. Display the numeric phone number
#
# Functions:
# - main(): handles user input and phone number conversion
#
# Logic:
# - Create list of digits: ['2','3','4','5','6','7','8','9']
# - Get alphabetic phone number from user input
# - Use for loop to iterate through each character in phone number
# - Check if character is a letter using isalpha()
# - If letter, convert to uppercase and determine digit mapping
# - Use if-elif chain to map letter groups to digits
# - Replace letter with corresponding digit
# - Keep non-letter characters unchanged
# - Build numeric phone number string
# - Display the final numeric phone number
#
# Letter to Digit Mapping:
# - ABC -> 2, DEF -> 3, GHI -> 4, JKL -> 5
# - MNO -> 6, PQRS -> 7, TUV -> 8, WXYZ -> 9
#
# String Operations:
# - for ch in string: - iterate through characters
# - ch.isalpha() - check if character is a letter
# - ch.upper() - convert to uppercase
# - string concatenation with '+'
#
# Example:
# Enter the telephone number in the format XXX-XXX-XXXX: 555-GET-FOOD
# The phone number is 555-438-3663
#
# Note: 
# - Program handles standard telephone keypad mapping
# - Preserves hyphens and other non-letter characters
# - Converts letters to uppercase for processing
# - Maintains XXX-XXX-XXXX format in output
