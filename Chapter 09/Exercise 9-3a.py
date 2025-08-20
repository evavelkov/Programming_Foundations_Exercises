# Programming Exercise 9-3a: File Encryption Program
#
# Task: Write a program that encrypts text files using a substitution cipher.
#
# Requirements:
# 1. Create a main function that handles file encryption and output
# 2. Create a convert function that performs the encryption
# 3. Define a CODE dictionary with character substitution mappings
# 4. Get input and output filenames from user
# 5. Read input file and encrypt its contents
# 6. Write encrypted text to output file
#
# Functions:
# - main(): handles file operations and calls convert function
# - convert(): reads input file and performs encryption
#
# Logic:
# - Define CODE dictionary with character substitution mappings
# - Get input filename from user
# - Get output filename from user
# - Call convert() function to get encrypted text
# - Open output file for writing
# - Write encrypted text to output file
# - In convert() function:
#   - Get input filename from user
#   - Open and read input file
#   - Process each character in the text
#   - If character is whitespace: keep unchanged
#   - If character is not whitespace: substitute using CODE dictionary
#   - Return encrypted text string
#
# Encryption Rules:
# - Letters are substituted with other letters or symbols
# - Numbers are substituted with other numbers or symbols
# - Punctuation marks are substituted with other punctuation
# - Whitespace characters (spaces, tabs, newlines) are preserved
# - Each character has a unique substitution mapping
#
# File Operations:
# - open(filename, 'r') - open file for reading
# - open(filename, 'w') - open file for writing
# - file.read() - read entire file content
# - file.write(text) - write text to file
# - with statement - automatic file closing
#
# Example:
# Enter the name of the input file: message.txt
# Enter the name of the output file: encrypted.txt
# (Creates encrypted.txt with substituted characters)
#
# Note: 
# - Program uses substitution cipher for encryption
# - Preserves whitespace characters
# - Handles all printable characters
# - Creates new encrypted file
# - Uses comprehensive character mapping
