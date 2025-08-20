# Design Exercise 6: Turtle Graphics - Geometric Pattern
#
# Task: Use turtle graphics to draw a complex geometric pattern with lines and dots.
#
# Requirements:
# 1. Import the turtle module
# 2. Define named constants for all coordinates:
#    - Upper left, upper right, lower left, lower right corners
#    - Center point
#    - GAP = 20 (for dotted lines)
# 3. Hide the turtle and set animation speed to 0
# 4. Draw solid lines connecting:
#    - Upper left to lower right
#    - Upper right to lower left
#    - Upper left to lower left
#    - Upper right to lower right
# 5. Draw dotted lines:
#    - Top edge (upper left to upper right) with gaps
#    - Bottom edge (lower left to lower right) with gaps
# 6. Add dots at:
#    - All four corners
#    - Center point
#
# Note: For dotted lines, alternate between pendown() and penup() with GAP distance
# Use turtle.dot() to place dots at specified coordinates
#
# Expected result: A geometric pattern with intersecting lines, dotted edges, and corner/center dots
