# Programming Exercise 9-6: Set Operations on Text Files
#
# Task: Write a program that performs set operations on words from two text files.
#
# Requirements:
# 1. Create a main function that handles file reading and set operations
# 2. Read words from two input files
# 3. Create sets of unique words from each file
# 4. Perform various set operations (union, intersection, difference, symmetric difference)
# 5. Display results of each set operation
#
# Functions:
# - main(): handles file operations and set operations
#
# Logic:
# - Get first input filename from user
# - Read first file and create set of unique words
# - Get second input filename from user
# - Read second file and create set of unique words
# - Perform set operations:
#   - Union: words in either file (set1.union(set2))
#   - Intersection: words in both files (set1.intersection(set2))
#   - Difference 1: words in first file but not second (set1.difference(set2))
#   - Difference 2: words in second file but not first (set2.difference(set1))
#   - Symmetric difference: words in either file but not both (set1.symmetric_difference(set2))
# - Display results of each operation with descriptive headers
#
# File Operations:
# - open(filename, 'r') - open file for reading
# - file.read() - read entire file content
# - with statement - automatic file closing
#
# String Operations:
# - string.split() - split text into words
#
# Set Operations:
# - set(words) - create set from word list
# - set1.union(set2) - get all unique words from both sets
# - set1.intersection(set2) - get words common to both sets
# - set1.difference(set2) - get words in set1 but not in set2
# - set2.difference(set1) - get words in set2 but not in set1
# - set1.symmetric_difference(set2) - get words in either set but not both
#
# Example:
# Enter the name of the first input file: file1.txt
# Enter the name of the second input file: file2.txt
# These are the unique words that are contained in both files:
# hello world python programming
#
# These are the words that appear both files:
# hello world
#
# These are the words that appear in the first file but do not appear in the second file:
# python
#
# These are the words that appear in the second file but do not appear in the first file:
# java
#
# These are the words that appear in the first file or the second file but do not appear in the both files:
# python java
#
# Note: 
# - Program reads two text files
# - Creates sets of unique words from each file
# - Demonstrates all major set operations
# - Provides clear descriptions for each result
# - Handles any text file format
