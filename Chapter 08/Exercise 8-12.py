# Programming Exercise 8-12: Pig Latin Converter
#
# Task: Write a program that converts text to Pig Latin.
#
# Requirements:
# 1. Create a main function that handles user input and Pig Latin conversion
# 2. Get a string from user input
# 3. Split the string into individual words
# 4. Convert each word to Pig Latin
# 5. Display the converted text
#
# Functions:
# - main(): handles user input and Pig Latin conversion
#
# Logic:
# - Get string from user input
# - Split string into words using split()
# - Use for loop to process each word
# - Convert each word to uppercase
# - Check word length:
#   - If one letter: just add 'AY' ending
#   - If more than one letter: move first letter to end and add 'AY'
# - Add converted word to result string
# - Add space between words (except after last word)
# - Display the final result
#
# Pig Latin Rules:
# - For one-letter words: add 'AY' (e.g., 'A' becomes 'AAY')
# - For multi-letter words: move first letter to end + 'AY' (e.g., 'HELLO' becomes 'ELLOHAY')
#
# String Operations:
# - string.split() - split into words
# - item.upper() - convert to uppercase
# - len(item) - get word length
# - item[1:] + item[0] - move first letter to end
# - string concatenation with '+'
#
# Example:
# Enter a string: Hello World
# ELLOHAY ORLDWAY
#
# Note: 
# - Program converts all words to uppercase
# - Handles single-letter and multi-letter words
# - Preserves word boundaries with spaces
# - Uses standard Pig Latin rules
# - Processes entire sentences
