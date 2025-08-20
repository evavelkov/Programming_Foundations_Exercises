# Programming Exercise 6-2: File Reading - First Five Lines
#
# Task: Write a program that reads and displays the first five lines of a user-specified file.
#
# Requirements:
# 1. Create a main function that handles file operations
# 2. Ask the user to enter a filename
# 3. Open the specified file for reading
# 4. Read and display only the first five lines
# 5. Use a while loop with a counter to limit output
# 6. Properly close the file
#
# Functions:
# - main(): handles user input, file operations, and display
#
# Logic:
# - Declare variables for line storage and counter
# - Get filename from user input
# - Open the specified file in read mode
# - Use priming read to get first line
# - Use while loop to read lines while counter <= 5
# - Strip newline characters from each line
# - Display each line
# - Close the file
#
# File Operations:
# - open(fileName, 'r') - opens user-specified file for reading
# - infile.readline() - reads one line at a time
# - line.rstrip('\n') - removes newline character
# - infile.close() - closes the file
#
# Example:
# Enter the name of the file: sample.txt
# (Displays first 5 lines of sample.txt)
#
# Note: Program should handle files with fewer than 5 lines gracefully
