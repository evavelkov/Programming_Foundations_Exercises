# Programming Exercise 8-8: Word Statistics Analyzer
#
# Task: Write a program that analyzes words in a file and calculates statistics.
#
# Requirements:
# 1. Create a main function that handles file reading and word analysis
# 2. Read words from 'words.txt' file (one word per line)
# 3. Count the total number of words
# 4. Find the longest word
# 5. Calculate the average word length
# 6. Display all statistics
#
# Functions:
# - main(): handles file operations and word analysis
#
# Logic:
# - Open 'words.txt' file for reading
# - Use for loop to read each word from file
# - Strip newline characters from each word
# - Count total number of words
# - Calculate length of each word
# - Track the longest word found
# - Calculate total length of all words
# - Calculate average length = total length / number of words
# - Close the file
# - Display all statistics with proper formatting
#
# File Operations:
# - open('words.txt', 'r') - opens file for reading
# - for word in infile: - iterates through file lines
# - infile.close() - closes the file
#
# String Operations:
# - word.rstrip('\n') - removes newline character
# - len(word) - gets word length
#
# Example:
# Number of Words: 150
# Longest Word: supercalifragilisticexpialidocious
# Average Word Length: 8
#
# Note: 
# - Program assumes 'words.txt' exists with one word per line
# - Manually opens and closes file (not using with statement)
# - Tracks longest word during processing
# - Calculates arithmetic mean of word lengths
# - Rounds average to nearest integer
