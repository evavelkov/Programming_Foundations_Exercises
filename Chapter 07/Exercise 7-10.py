# Programming Exercise 7-10: World Series Winner Search
#
# Task: Write a program that searches for World Series winners and counts their victories.
#
# Requirements:
# 1. Create a main function that handles file reading and team search
# 2. Read World Series winners from 'WorldSeriesWinners.txt' file
# 3. Get team name from user input
# 4. Search for team in winners list
# 5. Count number of victories for the team
# 6. Display search results
# 7. Implement comprehensive exception handling
#
# Functions:
# - main(): handles file operations, team search, and display
#
# Logic:
# - Use try-except block for error handling
# - Open 'WorldSeriesWinners.txt' file using with statement
# - Read all lines and strip newline characters
# - Get team name from user input
# - Check if team exists in winners list
# - If team not found, display appropriate message
# - If team found, count occurrences in list
# - Display victory count with proper formatting
#
# File Operations:
# - with open('WorldSeriesWinners.txt', 'r') as input_file: - opens file for reading
# - input_file.readlines() - reads all lines into list
# - line.rstrip('\n') - removes newline characters
#
# List Operations:
# - 'in' operator - checks if team exists in list
# - for loop with count - counts team occurrences
#
# Exception Handling:
# - FileNotFoundError: 'The file could not be found.'
# - IOError: 'There was an IO error.'
# - IndexError: 'There was an indexing error.'
# - General exception: 'An error occurred.'
#
# Output Format:
# - Team not found: 'The [team] never won the world series.'
# - Team found: 'The [team] won the world series [count] times between 1903 and 2009.'
#
# Example:
# Enter the name of a team: New York Yankees
# The New York Yankees won the world series 27 times between 1903 and 2009.
#
# Enter the name of a team: Seattle Mariners
# The Seattle Mariners never won the world series.
#
# Note: 
# - Program assumes 'WorldSeriesWinners.txt' exists with one winner per line
# - Covers years 1903-2009
# - Performs case-sensitive search
# - Counts all occurrences of team name in list
# - Implements comprehensive error handling
