# Programming Exercise 9-7: World Series Winner Lookup
#
# Task: Write a program that looks up World Series winners by year and provides statistics.
#
# Requirements:
# 1. Create a main function that handles file reading and winner lookup
# 2. Read World Series data from 'WorldSeriesWinners.txt' file
# 3. Create dictionaries to store year-to-winner and winner-to-count mappings
# 4. Handle skipped years (1904, 1994) appropriately
# 5. Get year from user input and display winner information
# 6. Show total wins for the winning team
#
# Functions:
# - main(): handles file operations and winner lookup
#
# Constants:
# - BASE_YEAR = 1903
#
# Logic:
# - Open 'WorldSeriesWinners.txt' file for reading
# - Read all lines into a list
# - Create two dictionaries:
#   - year_dict: maps year to winning team
#   - count_dict: maps team to number of wins
# - Process each line in the file:
#   - Calculate year based on line position and BASE_YEAR
#   - Adjust for skipped years (1904, 1994)
#   - Add year-team mapping to year_dict
#   - Update team win count in count_dict
# - Get year from user input
# - Check for special cases (1904, 1994, out of range)
# - Display winner and total wins for the team
#
# File Operations:
# - open('WorldSeriesWinners.txt', 'r') - open file for reading
# - file.readlines() - read all lines into list
# - line.rstrip('\n') - remove newline characters
#
# Dictionary Operations:
# - dictionary[key] = value - add key-value pair
# - key in dictionary - check if key exists
# - dictionary[key] += 1 - increment value
#
# Example:
# Enter a year in the range 1903-2009: 1927
# The team that won the world series in 1927 is the New York Yankees.
# They won the world series 27 times.
#
# Enter a year in the range 1903-2009: 1904
# The world series wasn't played in the year 1904.
#
# Note: 
# - Program handles skipped years (1904, 1994)
# - Validates year range (1903-2009)
# - Shows both winner and total wins for the team
# - Uses two dictionaries for efficient lookup
# - Provides appropriate error messages
