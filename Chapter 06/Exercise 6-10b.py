# Programming Exercise 6-10b: Golf Tournament Data Reader
#
# Task: Write a program that reads golf tournament data from a file and displays it.
#
# Requirements:
# 1. Create a main function that handles file reading and data display
# 2. Open 'golf.txt' file for reading
# 3. Read alternating lines (name, score) from the file
# 4. Display each player's name and golf score
# 5. Use with statement for file operations
#
# Functions:
# - main(): handles file reading and data display
#
# Logic:
# - Declare variables for line, name, and golf score
# - Use with statement to open 'golf.txt' file for reading
# - Use priming read to get first name
# - Use while loop to read until no more data
# - Read name and score pairs (alternating lines)
# - Convert score to integer
# - Strip newline characters from name
# - Display name and score using f-strings
# - Read next name for next iteration
# - Close file automatically with with statement
#
# File Operations:
# - with open('golf.txt', 'r') as infile: - opens file for reading
# - infile.readline() - reads one line at a time
# - name.rstrip('\n') - removes newline character from name
#
# Data Format:
# - File contains alternating lines: name, score, name, score, etc.
# - Each player's data is on two consecutive lines
#
# Output Format:
# - Name: [player name]
# - Golf Score: [score value]
#
# Example:
# Name: John Smith
# Golf Score: 72
# Name: Jane Doe
# Golf Score: 68
# Name: Bob Johnson
# Golf Score: 75
#
# Note: 
# - Program assumes 'golf.txt' exists with alternating name/score format
# - Uses with statement for automatic file closing
# - Part II of a two-part exercise (data display)
# - Reads data created by Exercise 6-10a
