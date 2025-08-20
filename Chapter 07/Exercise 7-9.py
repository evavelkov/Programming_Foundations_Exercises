# Programming Exercise 7-9: Population Change Analysis
#
# Task: Write a program that analyzes population changes from yearly data in a file.
#
# Requirements:
# 1. Create a main function that handles file reading and population analysis
# 2. Read population data from 'USPopulation.txt' file
# 3. Calculate yearly population changes
# 4. Find average annual change
# 5. Find years with greatest and smallest increases
# 6. Display analysis results
# 7. Implement comprehensive exception handling
#
# Functions:
# - main(): handles file operations, calculations, and display
#
# Logic:
# - Define BASE_YEAR constant (1950)
# - Use try-except block for error handling
# - Open 'USPopulation.txt' file using with statement
# - Read all lines and convert to float numbers
# - Calculate yearly changes (current year - previous year)
# - Track greatest and smallest increases with corresponding years
# - Calculate total and average changes
# - Display results with proper formatting
#
# File Operations:
# - with open('USPopulation.txt', 'r') as input_file: - opens file for reading
# - input_file.readlines() - reads all lines into list
# - float() conversion - converts strings to numbers
#
# Calculations:
# - Yearly change = current population - previous population
# - Total change = sum of all yearly changes
# - Average change = total change / number of changes
# - Year with greatest increase = BASE_YEAR + year index
# - Year with smallest increase = BASE_YEAR + year index
#
# Exception Handling:
# - FileNotFoundError: 'The file could not be found.'
# - IOError: 'There was an IO error.'
# - IndexError: 'There was an indexing error.'
# - General exception: 'An error occurred.'
#
# Output Format:
# - Average annual change with comma formatting and 2 decimal places
# - Year with greatest increase
# - Year with smallest increase
#
# Example:
# The average annual change in population during the time period is 2,443.75
# The year with the greatest increase in population was 1955
# The year with the smallest increase in population was 1957
#
# Note: 
# - Program assumes 'USPopulation.txt' exists with one population per line
# - Assumes all population changes are positive (increasing)
# - Uses BASE_YEAR constant for year calculations
# - Implements comprehensive error handling
