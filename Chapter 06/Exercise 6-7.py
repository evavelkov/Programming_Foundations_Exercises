# Programming Exercise 6-7: Random Number File Writer
#
# Task: Write a program that generates random numbers and writes them to a user-specified file.
#
# Requirements:
# 1. Import the random module
# 2. Create a main function that handles user input and file writing
# 3. Ask the user for a filename to write to
# 4. Ask the user for the number of random numbers to generate
# 5. Generate random numbers between 1 and 500
# 6. Write each random number to the file on a separate line
#
# Functions:
# - main(): handles user input, random generation, and file writing
#
# Logic:
# - Declare variables for filename and number count
# - Get filename from user input
# - Get number of random numbers from user input
# - Convert input to integer
# - Use with statement to open file for writing
# - Use for loop to generate specified number of random numbers
# - Generate random number between 1 and 500
# - Write each number to file with newline character
#
# File Operations:
# - with open(filename, 'w') as outputFile: - opens file for writing
# - outputFile.write(str(random_number) + '\n') - writes number with newline
#
# Random Generation:
# - random.randint(1, 500) - generates random integer between 1 and 500
#
# Example:
# Enter the name of the file to which results should be written: random_numbers.txt
# Enter the number of random numbers to be written to the file: 10
# (Creates file with 10 random numbers, one per line)
#
# Note: 
# - Program creates a new file or overwrites existing file
# - Each random number is written on a separate line
# - Uses with statement for automatic file closing
