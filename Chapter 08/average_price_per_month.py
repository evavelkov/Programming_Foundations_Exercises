# Programming Exercise: Average Price Per Month Gas Analysis
#
# Task: Write a program that analyzes gas prices and calculates monthly averages.
#
# Requirements:
# 1. Create multiple functions to extract data from gas price records
# 2. Create a main function that handles file reading and analysis
# 3. Read gas price data from 'GasPrices.txt' file
# 4. Calculate and display average prices for each month
# 5. Handle data in MM-DD-YYYY:Price format
#
# Functions:
# - get_price(str): extracts price from MM-DD-YYYY:Price format
# - get_month(str): extracts month from MM-DD-YYYY:Price format
# - get_year(str): extracts year from MM-DD-YYYY:Price format
# - display_monthly_averages(gas_list): calculates and displays monthly averages
# - main(): handles file operations and calls analysis function
#
# Logic:
# - Open 'GasPrices.txt' file using with statement
# - Read all lines into a list
# - Call display_monthly_averages function
# - In display_monthly_averages:
#   - Create list of month names
#   - Initialize variables for current month, year, total, count
#   - Use for loop to process each gas price record
#   - Check if record is for same month and year
#   - If same month/year: add price to total, increment count
#   - If different month/year: calculate and display average, reset counters
#   - Display average for last month
#
# Data Format:
# - Each line: MM-DD-YYYY:Price (e.g., "01-15-2020:2.45")
#
# String Operations:
# - str.split(':') - split at colon to separate date and price
# - str.split('-') - split date at hyphens
# - float() conversion - convert price to float
# - int() conversion - convert month/year to integer
#
# Example:
# Average price for January, 2020: $2.45
# Average price for February, 2020: $2.67
# ... (continues for all months)
#
# Note: 
# - Program assumes 'GasPrices.txt' exists with proper format
# - Uses with statement for automatic file closing
# - Handles multiple years of data
# - Calculates arithmetic mean for each month
# - Displays results with proper formatting
