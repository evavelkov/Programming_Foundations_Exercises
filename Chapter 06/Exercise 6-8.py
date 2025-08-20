# Programming Exercise 6-8: Word File Writer
#
# Task: Write a program that collects words from the user and writes them to a file.
#
# Requirements:
# 1. Create a main function that handles user input and file writing
# 2. Ask the user for the number of words to write
# 3. Collect each word from the user
# 4. Write each word to 'words.txt' file on a separate line
# 5. Display progress for each word entry
#
# Functions:
# - main(): handles user input, word collection, and file writing
#
# Logic:
# - Get number of words from user input
# - Convert input to integer
# - Open 'words.txt' file for writing
# - Use for loop to collect specified number of words
# - Display progress message for each word
# - Get word from user input
# - Write word to file with newline character
# - Close the file
#
# File Operations:
# - open('words.txt', 'w') - opens file for writing
# - outfile.write(word + '\n') - writes word with newline
# - outfile.close() - closes the file
#
# User Interface:
# - Display progress: 'Word X of Y - '
# - Use end='' to keep input on same line
#
# Example:
# Enter number of words to write: 3
# Word 1 of 3 - Enter a word: hello
# Word 2 of 3 - Enter a word: world
# Word 3 of 3 - Enter a word: python
# (Creates words.txt with three words, one per line)
#
# Note: 
# - Program creates 'words.txt' file or overwrites existing file
# - Each word is written on a separate line
# - Shows progress for each word entry
