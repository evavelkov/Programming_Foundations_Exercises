# Programming Exercise 7-8: Name Search
#
# Task: Write a program that searches for names in a list of popular names from a file.
#
# Requirements:
# 1. Create a main function that handles file reading and name search
# 2. Read names from 'popular_names.txt' file into a list
# 3. Get a name from user input
# 4. Search for the name in the list
# 5. Display search results
#
# Functions:
# - main(): handles file operations, name search, and display
#
# Logic:
# - Create empty list to store names
# - Open 'popular_names.txt' file using with statement
# - Read each line from file
# - Strip newline characters from each line
# - Append each name to the list
# - Get search name from user input
# - Use 'in' operator to search for name in list
# - Display appropriate result message
#
# File Operations:
# - with open('popular_names.txt', 'r') as name_file: - opens file for reading
# - for line in name_file: - iterates through file lines
# - line.rstrip('\n') - removes newline character
# - list.append() - adds names to list
#
# List Operations:
# - 'in' operator - checks if name exists in list
#
# Output Format:
# - Name found: 'That was a popular name between 2000 and 2009.'
# - Name not found: 'That was not a popular name between 2000 and 2009.'
#
# Example:
# Enter a name: Michael
# That was a popular name between 2000 and 2009.
#
# Enter a name: Zephyr
# That was not a popular name between 2000 and 2009.
#
# Note: 
# - Program assumes 'popular_names.txt' exists with one name per line
# - Uses with statement for automatic file closing
# - Performs case-sensitive search
# - Searches for exact name matches
