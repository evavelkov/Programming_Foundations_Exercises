# Programming Exercise: List of Prices Lowest to Highest Gas Analysis
#
# Task: Write a program that sorts gas prices from lowest to highest and creates a file.
#
# Requirements:
# 1. Create multiple functions to extract and sort gas price data
# 2. Create a main function that handles file reading and sorting
# 3. Read gas price data from 'GasPrices.txt' file
# 4. Sort prices from lowest to highest
# 5. Create 'low_to_high.txt' file with sorted data
# 6. Handle data in MM-DD-YYYY:Price format
#
# Functions:
# - get_price(str): extracts price from MM-DD-YYYY:Price format
# - get_date(str): extracts date from MM-DD-YYYY:Price format
# - lowest_element_position(g_list): finds position of lowest price in list
# - create_low_to_high_file(gas_list): creates sorted file from lowest to highest
# - main(): handles file operations and calls sorting function
#
# Logic:
# - Open 'GasPrices.txt' file using with statement
# - Read all lines into a list
# - Call create_low_to_high_file function
# - In create_low_to_high_file:
#   - Make copy of gas list
#   - Open 'low_to_high.txt' file for writing
#   - Use while loop while temp list has elements:
#     - Find position of lowest price using lowest_element_position
#     - Write lowest element to file
#     - Remove lowest element from temp list
#   - Close output file
#
# Data Format:
# - Each line: MM-DD-YYYY:Price (e.g., "01-15-2020:2.45")
#
# File Operations:
# - with open('GasPrices.txt', 'r') as gas_file: - opens input file for reading
# - open('low_to_high.txt', 'w') - opens output file for writing
# - outputfile.write() - writes data to output file
# - outputfile.close() - closes output file
#
# String Operations:
# - str.split(':') - split at colon to separate date and price
# - float() conversion - convert price to float
#
# Example:
# (Creates low_to_high.txt file with prices sorted from lowest to highest)
#
# Note: 
# - Program assumes 'GasPrices.txt' exists with proper format
# - Uses with statement for input file
# - Manually opens and closes output file
# - Uses selection sort algorithm to find lowest prices
# - Creates new file with sorted data
