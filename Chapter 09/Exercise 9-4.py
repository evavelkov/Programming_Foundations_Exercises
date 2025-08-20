# Programming Exercise 9-4: Unique Words Finder
#
# Task: Write a program that finds and displays unique words in a text file.
#
# Requirements:
# 1. Create a main function that handles file reading and word processing
# 2. Get input filename from user
# 3. Read text from the specified file
# 4. Split text into individual words
# 5. Create a set of unique words
# 6. Display all unique words
#
# Functions:
# - main(): handles file operations and word processing
#
# Logic:
# - Get input filename from user
# - Open input file for reading using with statement
# - Read entire file content into a string
# - Split text into words using split() method
# - Create set from words list to get unique words
# - Display header message
# - Use for loop to print each unique word
#
# File Operations:
# - open(filename, 'r') - open file for reading
# - file.read() - read entire file content
# - with statement - automatic file closing
#
# String Operations:
# - string.split() - split text into words (default splits on whitespace)
#
# Set Operations:
# - set(words) - create set from list to remove duplicates
# - for word in set - iterate through unique words
#
# Example:
# Enter the name of the input file: sample.txt
# These are the unique words in the text:
# hello
# world
# python
# programming
# is
# fun
#
# Note: 
# - Program reads entire file content
# - Splits text on whitespace to get words
# - Uses set to automatically remove duplicates
# - Displays each unique word on separate line
# - Handles any text file format
