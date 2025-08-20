# Programming Exercise 6-4: High Score Finder
#
# Task: Write a program that reads scores from a file and finds the highest score and its holder.
#
# Requirements:
# 1. Create a main function that handles file operations and score analysis
# 2. Open 'scores.txt' file for reading
# 3. Read alternating lines (name, score) from the file
# 4. Track the highest score and the person who achieved it
# 5. Count the total number of scores
# 6. Display the results
#
# Functions:
# - main(): handles file operations, score tracking, and display
#
# Logic:
# - Declare variables for high score, high scorer, and counter
# - Open 'scores.txt' file in read mode
# - Use priming read to get first name
# - Use while loop to read until no more data
# - Read name and score pairs (alternating lines)
# - Convert score to integer
# - Compare each score with current high score
# - Update high score and holder if current score is higher
# - Increment counter for each score
# - Close the file
# - Display high score, holder, and total count
#
# File Structure:
# - File contains alternating lines: name, score, name, score, etc.
# - Each name is on one line, each score is on the next line
#
# Output:
# - High Score: [highest score value]
# - Held By: [name of person with highest score]
# - Number of Scores: [total count of scores]
#
# Example:
# High Score: 95
# Held By: John Smith
# Number of Scores: 5
#
# Note: Program assumes 'scores.txt' exists with alternating name/score format
