# Programming Exercise 4-16: Turtle Graphics - Star Pattern
#
# Task: Write a turtle graphics program that draws a star pattern using lines.
#
# Requirements:
# 1. Import the turtle module
# 2. Set up the turtle with appropriate speed and hide it
# 3. Set the initial angle for the turtle
# 4. Use a for loop to draw 8 lines
# 5. Each line should be the same length
# 6. After each line, turn the turtle by a specific angle
#
# Constants:
# - INITIAL_ANGLE = 45 degrees
# - ANGLE_STEP = 135 degrees
# - NUM_LINES = 8
# - LENGTH = 200 units
# - ANIMATION_SPEED = 0
#
# Logic:
# - Use turtle.left(INITIAL_ANGLE) to set starting direction
# - Use for count in range(NUM_LINES) to draw 8 lines
# - Use turtle.forward(LENGTH) to draw each line
# - Use turtle.left(ANGLE_STEP) to turn after each line
#
# Result:
# - Creates an 8-pointed star pattern
# - Each line is 200 units long
# - Turtle turns 135 degrees after each line
