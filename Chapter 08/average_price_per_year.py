# Programming Exercise: Average Price Per Year Gas Analysis
#
# Task: Write a program that analyzes gas prices and calculates yearly averages.
#
# Requirements:
# 1. Create multiple functions to extract data from gas price records
# 2. Create a main function that handles file reading and analysis
# 3. Read gas price data from 'GasPrices.txt' file
# 4. Calculate and display average prices for each year (1993-2013)
# 5. Handle data in MM-DD-YYYY:Price format
#
# Functions:
# - get_price(str): extracts price from MM-DD-YYYY:Price format
# - get_month(str): extracts month from MM-DD-YYYY:Price format
# - get_day(str): extracts day from MM-DD-YYYY:Price format
# - get_year(str): extracts year from MM-DD-YYYY:Price format
# - get_yearly_average(gas_list, year): calculates average for specific year
# - main(): handles file operations and calls analysis function
#
# Constants:
# - STARTING_YEAR = 1993
# - ENDING_YEAR = 2013
#
# Logic:
# - Open 'GasPrices.txt' file using with statement
# - Read all lines into a list
# - Use for loop to process years from STARTING_YEAR to ENDING_YEAR
# - Call get_yearly_average function for each year
# - Display average price for each year
# - In get_yearly_average function:
#   - Initialize total and count variables
#   - Use for loop to process each gas price record
#   - Check if record is for specified year
#   - If match: add price to total, increment count
#   - Calculate and return average
#
# Data Format:
# - Each line: MM-DD-YYYY:Price (e.g., "01-15-2020:2.45")
#
# String Operations:
# - str.split(':') - split at colon to separate date and price
# - str.split('-') - split date at hyphens
# - float() conversion - convert price to float
# - int() conversion - convert date components to integers
#
# Example:
# The average price in 1993 was $1.07
# The average price in 1994 was $1.08
# ... (continues for all years 1993-2013)
#
# Note: 
# - Program assumes 'GasPrices.txt' exists with proper format
# - Uses with statement for automatic file closing
# - Processes specific year range (1993-2013)
# - Calculates arithmetic mean for each year
# - Displays results with proper formatting
