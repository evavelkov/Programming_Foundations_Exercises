# Programming Exercise 5-21: Turtle Graphics - Triangle Function
#
# Task: Write a turtle graphics program that draws colored triangles using functions.
#
# Requirements:
# 1. Import the turtle module
# 2. Create a triangle function that draws a filled triangle
# 3. Create a main function that sets up the turtle and calls triangle function
# 4. Draw three triangles with different colors and positions
# 5. Use the triangle function with coordinates and color parameters
#
# Functions:
# - main(): sets up turtle and calls triangle function
# - triangle(x1, y1, x2, y2, x3, y3, color): draws filled triangle
#
# Logic:
# - Set up turtle with appropriate speed and hide it
# - Define triangle function that takes 6 coordinates and a color
# - Use turtle.fillcolor() to set fill color
# - Use turtle.goto() to move to each vertex
# - Use turtle.begin_fill() and turtle.end_fill() for filled shapes
# - Call triangle function three times with different coordinates and colors
#
# Example:
# - Draw red triangle: (0,0) to (100,0) to (0,-100)
# - Draw green triangle: (0,0) to (-100,0) to (0,-100)
# - Draw blue triangle: (0,-100) to (-100,-200) to (100,-200)
#
# Result: Three colored triangles forming a pattern
