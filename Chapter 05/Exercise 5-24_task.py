# Programming Exercise 5-24: Turtle Graphics - Checkerboard Pattern
#
# Task: Write a turtle graphics program that draws a checkerboard pattern using functions.
#
# Requirements:
# 1. Import the turtle module
# 2. Create a square function that draws filled squares
# 3. Create a main function that draws a 5x5 checkerboard
# 4. Use nested loops to create alternating black and white squares
# 5. Set up the screen with appropriate dimensions
#
# Functions:
# - main(): sets up screen and draws checkerboard
# - square(x, y, width, color): draws filled square
#
# Constants:
# - SCREEN_WIDTH = 500, SCREEN_HEIGHT = 500
# - NUM_SQUARES_IN_A_ROW = 5, NUM_SQUARES_IN_A_COL = 5
# - SQUARE_WIDTH = calculated from screen width
#
# Logic:
# - Set up screen with specified dimensions
# - Calculate square width and starting positions
# - Use nested for loops to iterate through rows and columns
# - Alternate between black and white colors
# - Position each square at calculated coordinates
# - Use turtle.begin_fill() and turtle.end_fill() for filled squares
#
# Pattern:
# - 5x5 grid of squares
# - Alternating black and white colors
# - Each square is 100x100 pixels (500/5)
# - Covers the entire screen area
#
# Result: Complete checkerboard pattern with alternating colors
