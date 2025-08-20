# Programming Exercise: Frequency of Each Lottery Number
#
# Task: Write a program that analyzes lottery numbers and displays frequency of each number.
#
# Requirements:
# 1. Create a main function that handles file reading and frequency analysis
# 2. Create a get_numbers function that reads and processes lottery data
# 3. Read lottery numbers from 'pbnumbers.txt' file
# 4. Calculate frequency of each regular number (1-69) and PowerBall number (1-26)
# 5. Display frequency of each number
#
# Functions:
# - main(): handles file operations and frequency analysis
# - get_numbers(): reads and processes lottery data from file
#
# Constants:
# - LOTTERY_NUMBERS = 69 (regular numbers)
# - POWERBALL_NUMBERS = 26 (PowerBall numbers)
#
# Logic:
# - Call get_numbers() to get lottery data
# - Create frequency arrays for regular and PowerBall numbers
# - Process regular numbers:
#   - Use for loop to iterate through regular numbers
#   - Increment frequency array for each number
# - Process PowerBall numbers:
#   - Use for loop to iterate through PowerBall numbers
#   - Increment frequency array for each number
# - Display frequency of each regular number (1-69)
# - Display frequency of each PowerBall number (1-26)
#
# Data Format:
# - Each line: 5 regular numbers + 1 PowerBall number (e.g., "1 15 23 45 67 12")
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
# Frequencies of the regular numbers
# ----------------------------------
# 1 was chosen 15 times.
# 2 was chosen 12 times.
# ... (continues for numbers 1-69)
#
# Frequencies of the PowerBall numbers
# -----------------------------------
# 1 was chosen 8 times.
# 2 was chosen 10 times.
# ... (continues for numbers 1-26)
#
# Note: 
# - Program assumes 'pbnumbers.txt' exists with proper format
# - Uses with statement for automatic file closing
# - Tracks frequency of each number separately
# - Displays results in organized format
# - Handles both regular and PowerBall numbers
