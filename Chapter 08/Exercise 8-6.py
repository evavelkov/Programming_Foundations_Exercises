# Programming Exercise 8-6: Average Words Per Sentence Calculator
#
# Task: Write a program that calculates the average number of words per sentence in a file.
#
# Requirements:
# 1. Create a main function that handles file reading and calculations
# 2. Read sentences from 'text.txt' file
# 3. Count the number of sentences
# 4. Count the total number of words across all sentences
# 5. Calculate and display the average words per sentence
# 6. Implement proper exception handling
#
# Functions:
# - main(): handles file operations, calculations, and display
#
# Logic:
# - Use try-except block for error handling
# - Open 'text.txt' file using with statement
# - Read all lines from file into a list (each line is a sentence)
# - Count number of sentences (length of list)
# - Use for loop to process each sentence
# - Split each sentence into words using split()
# - Count words in each sentence and add to total
# - Calculate average = total words / number of sentences
# - Display the average with proper formatting
#
# File Operations:
# - with open('text.txt', 'r') as infile: - opens file for reading
# - infile.readlines() - reads all lines into list
#
# String Operations:
# - item.split() - split sentence into words
# - len(words) - count words in sentence
#
# Exception Handling:
# - FileNotFoundError: 'The file was not found.'
# - IOError: 'There was an IO error.'
# - General exception: 'An error occurred.'
#
# Example:
# Average number of words per line: 12.5
#
# Note: 
# - Program assumes 'text.txt' exists with one sentence per line
# - Uses with statement for automatic file closing
# - Implements comprehensive error handling
# - Calculates arithmetic mean of words per sentence
