# Programming Exercise 7-1: Valid Number Filter and Calculator
#
# Task: Write a program that filters numbers from a list and calculates statistics for valid numbers.
#
# Requirements:
# 1. Create a main function that processes a predefined list of numbers
# 2. Filter numbers to include only those between 0 and 100 (inclusive)
# 3. Calculate the total and average of valid numbers
# 4. Display the results with proper formatting
#
# Functions:
# - main(): handles list processing, filtering, and calculations
#
# Logic:
# - Declare a predefined list of numbers (including negative and over 100)
# - Create an empty list to store valid numbers
# - Use a for loop to iterate through the original list
# - Check if each number is between 0 and 100 (inclusive)
# - Append valid numbers to the new list
# - Add valid numbers to running total
# - Calculate average = total / number of valid numbers
# - Display total and average with 4 decimal places
#
# List Operations:
# - list.append() - add items to list
# - len() - get list length
# - sum() - calculate total (or manual addition)
#
# Output Format:
# - Total of valid numbers: [total]
# - Average of valid numbers: [average with 4 decimal places]
#
# Example:
# Total of valid numbers: 413
# Average of valid numbers: 51.6250
#
# Note: 
# - Program filters out negative numbers and numbers over 100
# - Only valid numbers (0-100) are included in calculations
# - Uses format() function for decimal precision
