# Programming Exercise 5-22: Turtle Graphics - Snowman Drawing
#
# Task: Write a turtle graphics program that draws a snowman using multiple functions.
#
# Requirements:
# 1. Import the turtle module
# 2. Create separate functions for each part of the snowman
# 3. Use global constants for all coordinates and dimensions
# 4. Draw a complete snowman with base, mid-section, arms, head, eyes, mouth, and hat
#
# Functions:
# - main(): calls all drawing functions
# - drawBase(): draws the bottom circle
# - drawMidSection(): draws the middle circle
# - drawArms(): draws both arms with multiple segments
# - drawHead(): draws head, eyes, and mouth
# - drawHat(): draws the hat with bottom and top parts
#
# Constants:
# - Various coordinates for all snowman parts
# - Radii for circles (base, mid-section, head, eyes)
# - Arm segment coordinates
# - Hat coordinates
#
# Logic:
# - Set up turtle with appropriate speed and hide it
# - Use turtle.circle() for circular parts
# - Use turtle.goto() and turtle.pendown() for line segments
# - Use turtle.begin_fill() and turtle.end_fill() for filled hat
# - Call each drawing function in sequence
#
# Result: Complete snowman drawing with all body parts and accessories
