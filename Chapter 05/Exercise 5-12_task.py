# Programming Exercise 5-12: Falling Distance Calculator
#
# Task: Write a program that calculates falling distance for objects using functions.
#
# Requirements:
# 1. Create a main function that displays a table of falling distances
# 2. Create a falling_distance function that calculates distance based on time
# 3. Use the physics formula for falling distance
# 4. Display falling distances for times 1-10 seconds
# 5. Format output as a table
#
# Functions:
# - main(): displays table and calls falling_distance()
# - falling_distance(time): calculates falling distance for given time
#
# Physics Formula:
# - distance = (9.8 * time²) / 2
# - Where 9.8 is gravitational acceleration (m/s²)
#
# Logic:
# - Use for loop to iterate through times 1-10 seconds
# - Call falling_distance function for each time
# - Calculate distance using physics formula
# - Display formatted table with time and distance
#
# Example output:
# Time	Falling Distance
# -----------------------------
# 1	4.90
# 2	19.60
# 3	44.10
# 4	78.40
# 5	122.50
# 6	176.40
# 7	240.10
# 8	313.60
# 9	396.90
# 10	490.00
