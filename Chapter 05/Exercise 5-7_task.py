# Programming Exercise 5-7: Paint Job Estimator
#
# Task: Write a program that estimates paint job costs using functions.
#
# Requirements:
# 1. Create a main function that handles input and calculations
# 2. Create a showCostEstimate function that displays cost breakdown
# 3. Use global constants for paint coverage and labor rates
# 4. Ask the user to enter wall space and paint price per gallon
# 5. Calculate gallons needed, labor hours, and costs
# 6. Display detailed cost estimate
#
# Constants:
# - FEET_PER_GALLON = 112 (square feet covered per gallon)
# - LABOR_HOURS = 8 (hours per gallon)
# - LABOR_CHARGE = 35 (dollars per hour)
#
# Functions:
# - main(): handles input, calculations, calls showCostEstimate()
# - showCostEstimate(gallonPaint, hourLabor, costPaint, costLabor): displays cost details
#
# Logic:
# - Get wall space and paint price from user
# - Calculate gallons needed = (wall space / 112) + 1 (round up)
# - Calculate labor hours = gallons * 8
# - Calculate paint cost = gallons * price per gallon
# - Calculate labor cost = labor hours * 35
# - Pass values to showCostEstimate function
# - Display formatted output with total cost
#
# Example:
# Enter wall space in square feet: 500
# Enter paint price per gallon: 25
# Gallons of paint: 5
# Hours of labor: 40
# Paint charges: $125.00
# Labor charges: $1,400.00
# Total cost: $1,525.00
