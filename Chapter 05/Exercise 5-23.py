# Programming Exercise 5-23: Turtle Graphics - Rectangular Pattern
#
# Task: Write a turtle graphics program that draws a complex rectangular pattern using functions.
#
# Requirements:
# 1. Import the turtle module
# 2. Create a rectangle function that draws filled rectangles
# 3. Create a rectangular_pattern function that draws nested rectangles with connecting lines
# 4. Ask the user to enter width and height
# 5. Draw a pattern with three nested rectangles and connecting lines
#
# Functions:
# - main(): gets user input and calls rectangular_pattern()
# - rectangle(x, y, width, height, color): draws filled rectangle
# - rectangular_pattern(width, height): creates the complete pattern
#
# Logic:
# - Get width and height from user
# - Draw outer rectangle (white)
# - Draw middle rectangle (white) - 1/8 inset from outer
# - Draw inner rectangle (black) - 1/4 inset from outer
# - Draw diagonal lines connecting outer corners to inner corners
# - Draw horizontal lines connecting middle of sides
# - Draw vertical lines connecting middle of top/bottom
#
# Pattern Elements:
# - Three nested rectangles with different sizes
# - Diagonal lines from outer to inner rectangle corners
# - Horizontal and vertical connecting lines
# - Different colors for visual contrast
#
# Example:
# Enter the width: 200
# Enter the height: 150
# (Draws complex rectangular pattern with connecting lines)
