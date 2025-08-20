# Programming Exercise 8-4: Morse Code Converter
#
# Task: Write a program that converts text to Morse code.
#
# Requirements:
# 1. Create a main function that handles user input and Morse code conversion
# 2. Create a list of Morse code patterns
# 3. Get text string from user input
# 4. Convert each character to its corresponding Morse code
# 5. Display Morse code with comma separators
#
# Functions:
# - main(): handles user input and Morse code conversion
#
# Logic:
# - Create list of Morse code patterns (space, punctuation, numbers, letters)
# - Get text string from user input
# - Use for loop to iterate through each character in string
# - Convert each character to uppercase
# - Use if-elif chain to determine Morse code index for each character
# - Display Morse code pattern with comma separator
# - Continue until all characters are processed
#
# Morse Code Mapping:
# - Space: index 0, Comma: index 1, Period: index 2, Question mark: index 3
# - Numbers 0-9: indices 4-13
# - Letters A-Z: indices 14-39
#
# String Operations:
# - for ch in string: - iterate through characters
# - ch.upper() - convert to uppercase
# - print with end='' - control output formatting
#
# Output Format:
# - Each Morse code pattern followed by comma
# - No space between patterns
# - All on same line
#
# Example:
# Enter the string to be converted to Morse code: HELLO
# ....,.,.-..,.-..,---,
#
# Note: 
# - Program handles letters, numbers, and basic punctuation
# - Converts all input to uppercase
# - Uses comprehensive if-elif chain for character mapping
# - Displays Morse code with comma separators
