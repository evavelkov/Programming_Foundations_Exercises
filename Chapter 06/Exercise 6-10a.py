# Programming Exercise 6-10a: Golf Tournament Data Writer
#
# Task: Write a program that collects golf tournament data and writes it to a file.
#
# Requirements:
# 1. Create a main function that handles user input and file writing
# 2. Ask the user for the number of players in the tournament
# 3. For each player, collect their name and golf score
# 4. Write the data to 'golf.txt' file in alternating format (name, score)
# 5. Use with statement for file operations
#
# Functions:
# - main(): handles user input, data collection, and file writing
#
# Logic:
# - Declare variables for name, golf score, and number of players
# - Get number of players from user input
# - Convert input to integer
# - Use with statement to open 'golf.txt' file for writing
# - Use for loop to collect data for each player
# - Get player name from user input
# - Get golf score from user input
# - Convert score to integer
# - Write name and score to file on separate lines
# - Close file automatically with with statement
#
# File Operations:
# - with open('golf.txt', 'w') as outfile: - opens file for writing
# - outfile.write(name + '\n') - writes name with newline
# - outfile.write(str(golf_score) + '\n') - writes score with newline
#
# Data Format:
# - Each player's data takes two lines: name, then score
# - File structure: name1, score1, name2, score2, etc.
#
# Example:
# Enter the number of players in the tournament: 3
# Enter the name of the player: John Smith
# Enter the golf score: 72
# Enter the name of the player: Jane Doe
# Enter the golf score: 68
# Enter the name of the player: Bob Johnson
# Enter the golf score: 75
# (Creates golf.txt with alternating name/score format)
#
# Note: 
# - Program creates 'golf.txt' file or overwrites existing file
# - Each player's data is written on two consecutive lines
# - Uses with statement for automatic file closing
# - Part I of a two-part exercise (data collection)
