# Programming Exercise 5-19: Number Guessing Game
#
# Task: Write a program that implements a number guessing game using functions.
#
# Requirements:
# 1. Import the random module
# 2. Create a main function that manages the game loop
# 3. Create a playGuessingGame function that handles individual games
# 4. Generate random numbers between 1 and 100
# 5. Allow user to guess numbers with feedback (too high/too low)
# 6. Allow user to quit by entering 0
#
# Functions:
# - main(): manages game loop and calls playGuessingGame()
# - playGuessingGame(number): handles individual guessing game
#
# Logic:
# - Use while loop to continue playing until user quits
# - Generate random number for each game
# - Get user's guess (1-100 or 0 to quit)
# - Provide feedback: "Too high", "Too low", or "Congratulations!"
# - Return to main loop when correct guess is made
# - Exit when user enters 0
#
# Example interaction:
# Enter a number between 1 and 100, or 0 to quit: 50
# Too high, try again
# Enter a number between 1 and 100, or 0 to quit: 25
# Too low, try again
# Enter a number between 1 and 100, or 0 to quit: 37
# Congratulations! You guessed the right number!
# Enter a number between 1 and 100, or 0 to quit: 0
# Thanks for playing!
