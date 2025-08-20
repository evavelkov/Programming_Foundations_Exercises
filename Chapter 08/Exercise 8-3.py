# Programming Exercise 8-3: Date Format Converter
#
# Task: Write a program that converts a date from mm/dd/yyyy format to long format.
#
# Requirements:
# 1. Create a main function that handles user input and date conversion
# 2. Create a list of month names
# 3. Get date in mm/dd/yyyy format from user input
# 4. Split the date string and extract components
# 5. Convert month number to month name
# 6. Display date in long format (Month Day, Year)
#
# Functions:
# - main(): handles user input and date conversion
#
# Logic:
# - Create list of month names: January through December
# - Get date string from user input (mm/dd/yyyy format)
# - Split date string using '/' as separator
# - Extract month, day, and year components
# - Convert month number to integer
# - Get month name from list using month number - 1 (0-based indexing)
# - Create long date string: month name + space + day + ', ' + year
# - Display the long date format
#
# String Operations:
# - string.split('/') - split string at '/' characters
# - list[index] - access list element
# - string concatenation with '+'
#
# List Operations:
# - month_list[month_num - 1] - get month name (adjust for 0-based indexing)
#
# Example:
# Enter a date in the format mm/dd/yyyy: 12/25/2023
# December 25, 2023
#
# Note: 
# - Program assumes valid date format input
# - Uses list indexing to convert month numbers to names
# - Handles all 12 months
# - Creates properly formatted long date string
