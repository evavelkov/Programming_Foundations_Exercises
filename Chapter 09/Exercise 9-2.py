# Programming Exercise 9-2: State Capitals Quiz Game
#
# Task: Write a program that quizzes users on state capitals.
#
# Requirements:
# 1. Import the random module
# 2. Create a main function that handles the quiz game
# 3. Create a dictionary with all 50 US states and their capitals
# 4. Generate random questions about state capitals
# 5. Track correct and incorrect responses
# 6. Allow user to quit the game
# 7. Display final score when quitting
#
# Functions:
# - main(): handles the quiz game logic
#
# Logic:
# - Initialize capitals dictionary with all 50 US states and capitals
# - Initialize counters for correct and incorrect responses
# - Use while loop to continue game until user quits
# - Generate random state for each question:
#   - Use random.randint(1,50) to get random number
#   - Use iterator to access state at random position
# - Get user's answer for the capital
# - Check if user wants to quit (enter '0')
# - Compare user's answer with correct capital
# - Update counters based on correctness
# - Display appropriate feedback message
# - Display final score when user quits
#
# Dictionary Operations:
# - dictionary[key] - access value for key
# - iter(dictionary) - create iterator for dictionary keys
# - iterator.__next__() - get next key from iterator
#
# Random Operations:
# - random.randint(1,50) - generate random number between 1 and 50
#
# Example:
# What is the capital of California? (or enter 0 to quit): Sacramento
# That is correct.
# What is the capital of Texas? (or enter 0 to quit): Austin
# That is correct.
# What is the capital of New York? (or enter 0 to quit): 0
# You had 2 correct responses and 0 incorrect responses.
#
# Note: 
# - Program includes all 50 US states and their capitals
# - Uses random selection for questions
# - Tracks score throughout the game
# - Allows user to quit at any time
# - Provides immediate feedback on answers
