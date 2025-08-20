# Programming Exercise 7-13: Magic 8 Ball Program
#
# Task: Write a program that simulates a Magic 8 Ball by providing random responses.
#
# Requirements:
# 1. Import the random module
# 2. Create a main function that handles file reading and response generation
# 3. Read responses from '8_ball_responses.txt' file
# 4. Get a question from user input
# 5. Display a random response from the list
#
# Functions:
# - main(): handles file operations, user input, and response display
#
# Logic:
# - Open '8_ball_responses.txt' file using with statement
# - Read all lines from file into a list
# - Strip newline characters from each response
# - Get question from user input
# - Generate random index within response list range
# - Display random response
#
# File Operations:
# - with open('8_ball_responses.txt', 'r') as response_file: - opens file for reading
# - response_file.readlines() - reads all lines into list
# - line.rstrip('\n') - removes newline characters
#
# Random Generation:
# - random.randint(0, len(responses)) - generates random index
# - Note: This should be len(responses) - 1 for proper indexing
#
# List Operations:
# - responses[index] - access random response
#
# Example:
# Enter your question: Will I pass my exam?
# It is certain.
#
# Enter your question: Should I go to the party?
# Don't count on it.
#
# Note: 
# - Program assumes '8_ball_responses.txt' exists with one response per line
# - Provides random responses regardless of the question
# - Uses with statement for automatic file closing
# - Simulates classic Magic 8 Ball toy functionality
