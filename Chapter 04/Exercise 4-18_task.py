# Programming Exercise 4-18: Turtle Graphics - STOP Sign
#
# Task: Write a turtle graphics program that draws a STOP sign (octagon) with text.
#
# Requirements:
# 1. Import math and turtle modules
# 2. Set up the graphics window with specific dimensions
# 3. Calculate the diameter of the octagon to center it
# 4. Position the turtle at the starting point
# 5. Draw an octagon using turtle graphics
# 6. Add "STOP" text in the center
#
# Constants:
# - WINDOW_WIDTH = 400, WINDOW_HEIGHT = 400
# - NUM_SIDES = 8, LENGTH = 100, ANGLE = 45
# - TEXT_X = -5, TEXT_Y = -10
# - ANIMATION_SPEED = 0
#
# Math Calculations:
# - Use Pythagorean theorem to calculate octagon diameter
# - diameter = s + 2 * x, where x = s / sqrt(2)
# - s = LENGTH (100 units)
#
# Logic:
# - Calculate starting position to center the octagon
# - Use for x in range(NUM_SIDES) to draw 8 sides
# - Use turtle.forward(LENGTH) and turtle.right(ANGLE)
# - Use turtle.write('STOP') to add text
#
# Result:
# - Draws a centered octagon (STOP sign shape)
# - Adds "STOP" text in the center
# - Sign is properly sized and positioned in the window
