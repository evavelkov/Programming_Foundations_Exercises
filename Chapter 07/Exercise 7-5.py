# Programming Exercise 7-5: Account Number Validator
#
# Task: Write a program that validates account numbers against a list from a file.
#
# Requirements:
# 1. Create a main function that handles file reading and validation
# 2. Read account numbers from 'charge_accounts.txt' file
# 3. Get an account number from user input
# 4. Check if the account number exists in the list
# 5. Display validation result
# 6. Implement proper exception handling
#
# Functions:
# - main(): handles file operations, validation, and display
#
# Logic:
# - Use try-except block for error handling
# - Open 'charge_accounts.txt' file using with statement
# - Read all lines from file into a list
# - Strip newline characters from each line
# - Get account number from user input
# - Use 'in' operator to check if account exists in list
# - Display appropriate validation message
# - Handle FileNotFoundError and other exceptions
#
# File Operations:
# - with open('charge_accounts.txt', 'r') as input_file: - opens file for reading
# - input_file.readlines() - reads all lines into list
# - line.rstrip('\n') - removes newline characters
#
# List Operations:
# - 'in' operator - checks if item exists in list
#
# Exception Handling:
# - FileNotFoundError: 'The file could not be found'
# - General exception: 'An error occurred'
#
# Output Format:
# - Valid account: 'Account number [number] is valid.'
# - Invalid account: 'Account number [number] is not valid.'
#
# Example:
# Enter the account number to be validated: 123456789
# Account number 123456789 is valid.
#
# Note: 
# - Program assumes 'charge_accounts.txt' exists with one account per line
# - Uses with statement for automatic file closing
# - Implements comprehensive error handling
# - Validates exact string matches
