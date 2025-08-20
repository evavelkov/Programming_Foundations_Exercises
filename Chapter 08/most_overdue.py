# Programming Exercise: Most Overdue Lottery Numbers
#
# Task: Write a program that analyzes lottery numbers and finds the most overdue numbers.
#
# Requirements:
# 1. Create multiple functions to analyze lottery number positions
# 2. Create a main function that handles file reading and analysis
# 3. Read lottery numbers from 'pbnumbers.txt' file
# 4. Track the last position where each number appeared
# 5. Find and display 10 most overdue numbers
#
# Functions:
# - get_all_numbers(): reads and processes lottery data from file
# - get_last_position(number_list, max_number): finds last position of each number
# - position_of_lowest_value(num_list): finds position of lowest value in list
# - most_overdue(pos_list): creates list sorted by most overdue to least overdue
# - main(): handles file operations and calls analysis functions
#
# Constants:
# - LOTTERY_NUMS = 69
# - MAX_NUM_OVERDUE = 10
#
# Logic:
# - Call get_all_numbers() to get lottery data
# - Call get_last_position() to find last position of each number
# - Call most_overdue() to get list sorted by overdue status
# - Determine number of overdue numbers to display (max 10)
# - Display most overdue numbers
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
# 10 Most Overdue Numbers
# -----------------------
# 67
# 34
# 89
# ... (continues for up to 10 numbers)
#
# Note: 
# - Program assumes 'pbnumbers.txt' exists with proper format
# - Uses with statement for automatic file closing
# - Tracks last appearance position of each number 1-69
# - Numbers with lowest last position are most overdue
# - Displays up to 10 most overdue numbers
