# Programming Exercise 5-20: Rock, Paper, Scissors Game
#
# Task: Write a program that implements a Rock, Paper, Scissors game using functions.
#
# Requirements:
# 1. Import the random module
# 2. Create a main function that manages the game
# 3. Create a rockPaperScissors function that determines the winner
# 4. Create a choiceString function that converts numbers to choice names
# 5. Use global constants for game choices and outcomes
# 6. Continue playing until there's a winner (no tie)
#
# Constants:
# - ROCK = 1, PAPER = 2, SCISSORS = 3
# - COMPUTER_WINS = 1, PLAYER_WINS = 2, TIE = 0, INVALID = 3
#
# Functions:
# - main(): manages game loop and displays results
# - rockPaperScissors(computer, player): determines winner
# - choiceString(choice): converts number to choice name
#
# Game Rules:
# - Rock beats Scissors, Scissors beats Paper, Paper beats Rock
# - Same choices result in a tie (game continues)
# - Invalid choices result in no winner
#
# Logic:
# - Generate random computer choice (1-3)
# - Get player choice from user
# - Display both choices using choiceString function
# - Determine winner using rockPaperScissors function
# - Continue if tie, display winner otherwise
#
# Example:
# Enter 1 for rock, 2 for paper, 3 for scissors: 2
# Computer chose rock
# You chose paper
# You win the game
