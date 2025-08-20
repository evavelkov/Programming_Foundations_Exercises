# Programming Exercise 7-6: Dice Rolling Simulator
#
# Task: Write a program that simulates rolling multiple dice and returns sorted results.
#
# Requirements:
# 1. Import the random module
# 2. Create a main function that handles user input and calls roll function
# 3. Create a roll function that generates random dice rolls
# 4. Get number of dice from user input
# 5. Generate random numbers between 1 and 6 for each die
# 6. Return sorted list of dice results
#
# Functions:
# - main(): handles user input and displays results
# - roll(num): generates and returns sorted list of dice rolls
#
# Logic:
# - Get number of dice from user input
# - Convert input to integer
# - Call roll function with number of dice
# - Display the returned list
# - In roll function:
#   - Create empty list for dice results
#   - Use for loop to generate specified number of rolls
#   - Generate random number between 1 and 6
#   - Append each roll to list
#   - Sort the list
#   - Return sorted list
#
# Random Generation:
# - random.randint(1, 6) - generates random integer between 1 and 6
#
# List Operations:
# - list.append() - add dice rolls to list
# - list.sort() - sort list in ascending order
#
# Example:
# Enter a positive integer: 5
# [2, 3, 4, 5, 6]
#
# Note: 
# - Program simulates standard 6-sided dice
# - Returns sorted list of results
# - Handles any positive integer input
# - Uses random.randint() for fair dice simulation
