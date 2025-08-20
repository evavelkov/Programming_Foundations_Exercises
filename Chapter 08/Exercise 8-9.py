# Programming Exercise 8-9: Vowel and Consonant Counter
#
# Task: Write a program that counts vowels and consonants in a string.
#
# Requirements:
# 1. Create a main function that handles user input and calls counting functions
# 2. Create a vowel_counter function that counts vowels in a string
# 3. Create a consonant_counter function that counts consonants in a string
# 4. Get a string from user input
# 5. Display the counts of vowels and consonants
#
# Functions:
# - main(): handles user input and displays results
# - vowel_counter(string): counts vowels in string
# - consonant_counter(string): counts consonants in string
#
# Logic:
# - Get string from user input
# - Call vowel_counter function and store result
# - Call consonant_counter function and store result
# - Display both counts
# - In vowel_counter function:
#   - Define vowels string: 'aeiou'
#   - Use for loop to iterate through each character
#   - Use find() method to check if character is a vowel
#   - Count vowels and return total
# - In consonant_counter function:
#   - Define consonants string: 'bcdfghjklmnpqrstvwxyz'
#   - Use for loop to iterate through each character
#   - Use find() method to check if character is a consonant
#   - Count consonants and return total
#
# String Operations:
# - for ch in string: - iterate through characters
# - vowels.find(ch) - check if character is in vowels string
# - consonants.find(ch) - check if character is in consonants string
#
# Example:
# Enter a string: Hello World
# The string you entered includes 3 vowels and 7 consonants.
#
# Note: 
# - Program counts only alphabetic characters
# - Ignores spaces, punctuation, and numbers
# - Uses find() method to check character membership
# - Handles both uppercase and lowercase letters
# - Assumes input contains only letters, spaces, and punctuation
