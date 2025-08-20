# Programming Exercise: Highest and Lowest Prices Per Year Gas Analysis
#
# Task: Write a program that analyzes gas prices and finds highest and lowest prices for each year.
#
# Requirements:
# 1. Create multiple functions to extract data from gas price records
# 2. Create a main function that handles file reading and analysis
# 3. Read gas price data from 'GasPrices.txt' file
# 4. Find and display highest price for each year
# 5. Find and display lowest price for each year
# 6. Handle data in MM-DD-YYYY:Price format
#
# Functions:
# - get_price(str): extracts price from MM-DD-YYYY:Price format
# - get_year(str): extracts year from MM-DD-YYYY:Price format
# - display_highest_per_year(gas_list): finds and displays highest prices per year
# - display_lowest_per_year(gas_list): finds and displays lowest prices per year
# - main(): handles file operations and calls analysis functions
#
# Logic:
# - Open 'GasPrices.txt' file using with statement
# - Read all lines into a list
# - Call display_highest_per_year function
# - Call display_lowest_per_year function
# - In display_highest_per_year:
#   - Initialize current year and highest price
#   - Use for loop to process each gas price record
#   - Check if record is for same year
#   - If same year: update highest if current price is higher
#   - If different year: display highest for previous year, reset for new year
#   - Display highest for last year
# - In display_lowest_per_year:
#   - Similar logic but track lowest prices instead
#
# Data Format:
# - Each line: MM-DD-YYYY:Price (e.g., "01-15-2020:2.45")
#
# String Operations:
# - str.split(':') - split at colon to separate date and price
# - str.split('-') - split date at hyphens
# - float() conversion - convert price to float
# - int() conversion - convert year to integer
#
# Example:
# Highest price for 2020: $3.45
# Highest price for 2021: $3.67
# ... (continues for all years)
#
# Lowest price for 2020: $2.15
# Lowest price for 2021: $2.23
# ... (continues for all years)
#
# Note: 
# - Program assumes 'GasPrices.txt' exists with proper format
# - Uses with statement for automatic file closing
# - Handles multiple years of data
# - Tracks highest and lowest prices separately
# - Displays results with proper formatting
