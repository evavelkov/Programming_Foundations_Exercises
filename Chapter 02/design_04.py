# Design Exercise 4: Turtle Graphics - Circle Pattern
#
# Task: Use turtle graphics to draw a pattern of 5 circles in a wave-like formation.
#
# Requirements:
# 1. Import the turtle module
# 2. Define named constants:
#    - RADIUS = 100
#    - STARTING_POINT_X = -250, STARTING_POINT_Y = 0
#    - HSHIFT = 125 (horizontal shift between circles)
#    - VSHIFT = 100 (vertical shift for alternating circles)
# 3. Draw 5 circles in sequence:
#    - Circle 1: at starting position (x, y)
#    - Circle 2: x += HSHIFT, y -= VSHIFT
#    - Circle 3: x += HSHIFT, y = 0
#    - Circle 4: x += HSHIFT, y -= VSHIFT
#    - Circle 5: x += HSHIFT, y = 0
# 4. Use penup() and pendown() to move between circles
#
# Note: Each circle should be drawn using turtle.circle(RADIUS)
#
# Expected result: A wave-like pattern of 5 circles alternating up and down
