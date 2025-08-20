# Programming Exercise 7-3: Rainfall Data Analysis
#
# Task: Write a program that collects monthly rainfall data and calculates statistics.
#
# Requirements:
# 1. Create a main function that handles data collection and analysis
# 2. Create lists for month names and rainfall amounts
# 3. Collect rainfall data for each month from user input
# 4. Calculate total, average, highest, and lowest rainfall
# 5. Display results with proper formatting
#
# Functions:
# - main(): handles data collection, calculations, and display
#
# Logic:
# - Create list of month names: January through December
# - Create list to store rainfall amounts (12 zeros)
# - Use for loop to collect rainfall for each month
# - Get user input for each month's rainfall
# - Convert input to float and store in list
# - Calculate total rainfall using sum()
# - Calculate average = total / 12
# - Find highest rainfall using max()
# - Find lowest rainfall using min()
# - Find indices of highest and lowest months
# - Display all results with f-strings
#
# List Operations:
# - sum() - calculate total
# - max() - find maximum value
# - min() - find minimum value
# - index() - find position of value in list
#
# Output Format:
# - Total rainfall: [total with 2 decimal places]
# - Average rainfall: [average with 2 decimal places]
# - Highest rainfall: [month name]
# - Lowest rainfall: [month name]
#
# Example:
# Enter the rainfall for January: 2.5
# Enter the rainfall for February: 3.2
# ... (continues for all 12 months)
# Total rainfall: 45.67
# Average rainfall: 3.81
# Highest rainfall: June
# Lowest rainfall: December
#
# Note: 
# - Program collects data for all 12 months
# - Uses list indexing to match months with rainfall data
# - Handles decimal rainfall amounts
# - Uses built-in list functions for calculations
