# Programming Exercise 9-10: Text Index Generator
#
# Task: Write a program that creates an index of words and their line numbers from a text file.
#
# Requirements:
# 1. Create a main function that handles file reading and index creation
# 2. Create a get_word_dict function that builds word-to-line-numbers mapping
# 3. Create a write_index_file function that writes the index to a file
# 4. Read text from 'Kennedy.txt' file
# 5. Generate index showing each word and its line numbers
# 6. Write index to 'index.txt' file
#
# Functions:
# - main(): handles file operations and calls helper functions
# - get_word_dict(line_list): creates dictionary mapping words to line numbers
# - write_index_file(word_dict): writes index to output file
#
# Logic:
# - Open 'Kennedy.txt' file and read all lines into a list
# - Strip newline characters from each line
# - Call get_word_dict() to create word-to-line-numbers mapping
# - Call write_index_file() to write index to file
# - In get_word_dict():
#   - Initialize empty dictionary and line counter
#   - Process each line in the list
#   - Split line into words
#   - For each word: add to dictionary with line number
#   - Use sets to store multiple line numbers for same word
# - In write_index_file():
#   - Open 'index.txt' for writing
#   - Write each word followed by its line numbers
#   - Close the file
#
# File Operations:
# - open('Kennedy.txt', 'r') - open input file for reading
# - open('index.txt', 'w') - open output file for writing
# - file.readlines() - read all lines into list
# - file.write(text) - write text to file
# - file.close() - close file
# - with statement - automatic file closing
#
# String Operations:
# - line.rstrip('\n') - remove newline character
# - line.split(' ') - split line into words
#
# Dictionary Operations:
# - dictionary[key] = value - add key-value pair
# - key in dictionary - check if key exists
# - dictionary[key].add(value) - add value to set
# - set([value]) - create set with single value
#
# Example:
# (Creates index.txt with format:)
# word1: 1 3 5
# word2: 2 4
# word3: 1 2 6
#
# Note: 
# - Program reads entire text file
# - Creates comprehensive word index
# - Uses sets to store multiple line numbers per word
# - Writes formatted index to output file
# - Handles words that appear multiple times
