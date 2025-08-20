# Programming Exercise 7-4: Number List Statistics Calculator
#
# Task: Write a program that collects 20 numbers and calculates various statistics.
#
# Requirements:
# 1. Create a main function that handles data collection and calculations
# 2. Collect 20 numbers from user input
# 3. Store numbers in a list
# 4. Calculate low, high, total, and average
# 5. Display results with proper formatting
#
# Functions:
# - main(): handles data collection, calculations, and display
#
# Logic:
# - Create empty list to store numbers
# - Use for loop to collect 20 numbers from user
# - Display prompt with current number (1-20)
# - Convert input to float and append to list
# - Calculate low value using min()
# - Calculate high value using max()
# - Calculate total using sum()
# - Calculate average = total / 20
# - Display all results with f-strings and formatting
#
# List Operations:
# - list.append() - add numbers to list
# - min() - find minimum value
# - max() - find maximum value
# - sum() - calculate total
#
# Output Format:
# - Low: [minimum value]
# - High: [maximum value]
# - Total: [total with comma formatting and 2 decimal places]
# - Average: [average with comma formatting and 2 decimal places]
#
# Example:
# Enter number 1 of 20: 15.5
# Enter number 2 of 20: 23.7
# ... (continues for all 20 numbers)
# Low: 5.2
# High: 89.3
# Total: 456.78
# Average: 22.84
#
# Note: 
# - Program collects exactly 20 numbers
# - Uses list.append() to build the list dynamically
# - Handles decimal numbers
# - Uses comma formatting for large numbers
# - Shows progress (number X of 20) during input
