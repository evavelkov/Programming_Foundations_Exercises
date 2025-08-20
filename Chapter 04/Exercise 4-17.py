# Programming Exercise 4-17: Turtle Graphics - Spiral Pattern
#
# Task: Write a turtle graphics program that draws a spiral pattern with increasing line lengths.
#
# Requirements:
# 1. Import the turtle module
# 2. Set up the turtle with appropriate speed and hide it
# 3. Use a for loop to draw lines with increasing lengths
# 4. Start with a short line and gradually increase the length
# 5. Turn the turtle after each line
#
# Constants:
# - ANIMATION_SPEED = 0
# - NUM_LINES = 50 (calculated from range)
# - STARTING_LENGTH = 1
# - ENDING_LENGTH = 500
# - STEP = 10
# - ANGLE = 90 degrees
#
# Logic:
# - Use for x in range(STARTING_LENGTH, ENDING_LENGTH, STEP)
# - Use turtle.forward(x) to draw line of length x
# - Use turtle.left(ANGLE) to turn after each line
# - Line lengths increase: 1, 11, 21, 31, ..., 491
#
# Result:
# - Creates a spiral pattern
# - Each line is 10 units longer than the previous
# - Turtle turns 90 degrees after each line
# - Pattern grows outward in a square spiral
