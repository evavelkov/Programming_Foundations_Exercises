# Programming Exercise 9-5: Random Number Frequency Counter
#
# Task: Write a program that generates random numbers and counts their frequencies.
#
# Requirements:
# 1. Import the random module
# 2. Create a main function that handles random number generation and counting
# 3. Generate 100 random numbers between 1 and 10
# 4. Count frequency of each number using a dictionary
# 5. Display results in a formatted table
#
# Functions:
# - main(): handles random number generation and frequency counting
#
# Logic:
# - Initialize empty dictionary to store number frequencies
# - Use for loop to generate 100 random numbers
# - For each random number:
#   - Generate number between 1 and 10 using random.randint(1, 10)
#   - Check if number exists in dictionary
#   - If not exists: add to dictionary with count 1
#   - If exists: increment count by 1
# - Display formatted table header
# - Use sorted() function to sort dictionary items
# - Display each number and its frequency in tabular format
#
# Random Operations:
# - random.randint(1, 10) - generate random integer between 1 and 10
#
# Dictionary Operations:
# - number not in dictionary - check if key exists
# - dictionary[number] = 1 - add new key with initial count
# - dictionary[number] += 1 - increment existing count
# - sorted(dictionary.items()) - get sorted list of key-value pairs
#
# Example:
# Number	Frequency
# ------  ---------
# 1	12
# 2	8
# 3	15
# 4	11
# 5	9
# 6	13
# 7	10
# 8	7
# 9	14
# 10	11
#
# Note: 
# - Program generates exactly 100 random numbers
# - Numbers range from 1 to 10 inclusive
# - Uses dictionary to track frequency of each number
# - Displays results in sorted order
# - Shows tabular format with proper alignment
