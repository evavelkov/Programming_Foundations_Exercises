# Programming Exercise: List of Prices Highest to Lowest Gas Analysis
#
# Task: Write a program that sorts gas prices from highest to lowest and creates a file.
#
# Requirements:
# 1. Create multiple functions to extract and sort gas price data
# 2. Create a main function that handles file reading and sorting
# 3. Read gas price data from 'GasPrices.txt' file
# 4. Sort prices from highest to lowest
# 5. Create 'high_to_low.txt' file with sorted data
# 6. Handle data in MM-DD-YYYY:Price format
#
# Functions:
# - get_price(str): extracts price from MM-DD-YYYY:Price format
# - get_date(str): extracts date from MM-DD-YYYY:Price format
# - highest_element_position(g_list): finds position of highest price in list
# - create_high_to_low_file(gas_list): creates sorted file from highest to lowest
# - main(): handles file operations and calls sorting function
#
# Logic:
# - Open 'GasPrices.txt' file using with statement
# - Read all lines into a list
# - Call create_high_to_low_file function
# - In create_high_to_low_file:
#   - Make copy of gas list
#   - Open 'high_to_low.txt' file for writing
#   - Use while loop while temp list has elements:
#     - Find position of highest price using highest_element_position
#     - Write highest element to file
#     - Remove highest element from temp list
#   - Close output file
#
# Data Format:
# - Each line: MM-DD-YYYY:Price (e.g., "01-15-2020:2.45")
#
# File Operations:
# - with open('GasPrices.txt', 'r') as gas_file: - opens input file for reading
# - open('high_to_low.txt', 'w') - opens output file for writing
# - outputfile.write() - writes data to output file
# - outputfile.close() - closes output file
#
# String Operations:
# - str.split(':') - split at colon to separate date and price
# - float() conversion - convert price to float
#
# Example:
# (Creates high_to_low.txt file with prices sorted from highest to lowest)
#
# Note: 
# - Program assumes 'GasPrices.txt' exists with proper format
# - Uses with statement for input file
# - Manually opens and closes output file
# - Uses selection sort algorithm to find highest prices
# - Creates new file with sorted data
