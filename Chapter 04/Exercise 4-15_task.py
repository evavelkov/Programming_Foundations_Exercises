# Programming Exercise 4-15: Turtle Graphics - Square Pattern
#
# Task: Write a turtle graphics program that draws a pattern of increasing squares.
#
# Requirements:
# 1. Import the turtle module
# 2. Set up the turtle with appropriate speed and hide it
# 3. Use nested for loops to draw 50 squares
# 4. Each square should be larger than the previous one
# 5. Each square should be positioned differently
# 6. Draw each square using turtle graphics commands
#
# Constants:
# - STARTING_X = -4, STARTING_Y = 4, STARTING_SIZE = 8
# - NUM_SQUARES = 50, STEP = 4, NUM_SIDES = 4, ANGLE = 90
# - ANIMATION_SPEED = 0
#
# Logic:
# - Use for count in range(NUM_SQUARES) for the outer loop
# - Position turtle at (x, y) coordinates
# - Use for s in range(NUM_SIDES) to draw each square
# - Use turtle.forward(size) and turtle.right(ANGLE)
# - Update x, y, and size for the next square
#
# Pattern:
# - Each square increases in size by STEP
# - X coordinate decreases by STEP
# - Y coordinate increases by STEP
# - Creates a spiral-like pattern of growing squares
