# Programming Exercise: Most and Least Common Lottery Numbers
#
# Task: Write a program that analyzes lottery numbers and finds most and least common numbers.
#
# Requirements:
# 1. Create multiple functions to analyze lottery number frequencies
# 2. Create a main function that handles file reading and analysis
# 3. Read lottery numbers from 'pbnumbers.txt' file
# 4. Calculate frequency of each number (1-69)
# 5. Find and display 10 most common numbers
# 6. Find and display 10 least common numbers
#
# Functions:
# - get_all_numbers(): reads and processes lottery data from file
# - get_frequency(number_list, max_value): calculates frequency of each number
# - position_of_highest_value(num_list): finds position of highest value in list
# - most_common(freq_list): creates list sorted by most common to least common
# - main(): handles file operations and calls analysis functions
#
# Constants:
# - LOTTERY_NUMBERS = 69
#
# Logic:
# - Call get_all_numbers() to get lottery data
# - Call get_frequency() to calculate frequency of each number
# - Call most_common() to get list sorted by frequency
# - Display 10 most common numbers (highest to lowest frequency)
# - Reverse the sorted list
# - Display 10 least common numbers (lowest to highest frequency)
#
# Data Format:
# - Each line: 6 lottery numbers (e.g., "1 15 23 45 67 12")
#
# File Operations:
# - with open('pbnumbers.txt', 'r') as pblottery_file: - opens file for reading
# - pblottery_file.readlines() - reads all lines into list
# - line.rstrip('\n') - removes newline characters
#
# String Operations:
# - line.split() - splits line into individual numbers
# - int() conversion - converts strings to integers
#
# Example:
# 10 Most Common Numbers (Highest to Lowest)
# -----------------------------------------
# 23
# 45
# 12
# ... (continues for 10 numbers)
#
# 10 Least Common Numbers (Lowest to Highest)
# -----------------------------------------
# 67
# 34
# 89
# ... (continues for 10 numbers)
#
# Note: 
# - Program assumes 'pbnumbers.txt' exists with proper format
# - Uses with statement for automatic file closing
# - Analyzes frequency of all numbers 1-69
# - Sorts numbers by frequency (most to least common)
# - Displays top and bottom 10 numbers
