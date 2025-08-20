# Programming Exercise 3-18: Hit the Target Game
#
# Task: Write a turtle graphics game where the user launches a projectile to hit a target.
#
# Requirements:
# 1. Import the turtle module
# 2. Set up the game window and draw a target square
# 3. Ask the user to enter the projectile's angle
# 4. Ask the user to enter the launch force (1-10)
# 5. Calculate the distance using: distance = force * FORCE_FACTOR
# 6. Launch the projectile using turtle graphics
# 7. Check if the projectile hit the target
# 8. Display appropriate messages and hints based on the result
#
# Constants:
# - SCREEN_WIDTH = 600, SCREEN_HEIGHT = 600
# - TARGET_LLEFT_X = 100, TARGET_LLEFT_Y = 250
# - TARGET_WIDTH = 25
# - FORCE_FACTOR = 30
# - NORTH = 90, SOUTH = 270, EAST = 0, WEST = 180
#
# Game Logic:
# - Draw target square at specified coordinates
# - Use turtle.setheading(angle) and turtle.forward(distance)
# - Check if turtle position is within target bounds
# - Provide hints based on where the projectile landed
#
# Example:
# Enter the projectile's angle: 45
# Enter the launch force (1-10): 5
# You missed the target.
# Try a greater angle.
