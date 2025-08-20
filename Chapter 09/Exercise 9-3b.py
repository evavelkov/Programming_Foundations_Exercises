# Programming Exercise 9-3b: File Decryption Program
#
# Task: Write a program that decrypts text files using a substitution cipher.
#
# Requirements:
# 1. Create a main function that handles file decryption and display
# 2. Create a convert function that performs the decryption
# 3. Define a CODE dictionary with character substitution mappings
# 4. Get input filename from user
# 5. Read input file and decrypt its contents
# 6. Display decrypted text on screen
#
# Functions:
# - main(): handles file operations and calls convert function
# - convert(): reads input file and performs decryption
#
# Logic:
# - Define CODE dictionary with character substitution mappings
# - Get input filename from user
# - Call convert() function to get decrypted text
# - Display decrypted text on screen
# - In convert() function:
#   - Get input filename from user
#   - Open and read input file
#   - Process each character in the text
#   - If character is whitespace: keep unchanged
#   - If character is not whitespace: substitute using CODE dictionary
#   - Return decrypted text string
#
# Decryption Rules:
# - Uses same substitution mapping as encryption (inverse operation)
# - Letters are substituted with their original characters
# - Numbers are substituted with their original numbers
# - Punctuation marks are substituted with original punctuation
# - Whitespace characters (spaces, tabs, newlines) are preserved
# - Each encrypted character is mapped back to its original
#
# File Operations:
# - open(filename, 'r') - open file for reading
# - file.read() - read entire file content
# - with statement - automatic file closing
#
# Example:
# Enter the name of the input file: encrypted.txt
# (Displays decrypted text on screen)
#
# Note: 
# - Program uses same substitution cipher as encryption
# - Preserves whitespace characters
# - Handles all printable characters
# - Displays decrypted text instead of saving to file
# - Uses inverse character mapping for decryption
