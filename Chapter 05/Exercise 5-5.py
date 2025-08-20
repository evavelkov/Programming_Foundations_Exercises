# Programming Exercise 5-5: Property Tax Calculator
#
# Task: Write a program that calculates property tax using functions.
#
# Requirements:
# 1. Create a main function that handles input and calculations
# 2. Create a showPropertyTax function that displays tax information
# 3. Use global constants for assessment and tax percentages
# 4. Ask the user to enter the actual property value
# 5. Calculate assessed value and property tax
# 6. Display the tax breakdown
#
# Constants:
# - ASSESS_PERCENT = 0.6 (60% of actual value)
# - PROPERTY_TAX_PERCENT = 0.0072 (0.72% of assessed value)
#
# Functions:
# - main(): handles input, calculations, calls showPropertyTax()
# - showPropertyTax(assessValue, propertyTax): displays tax details
#
# Logic:
# - Get actual property value from user
# - Calculate assessed value = actual value * 0.6
# - Calculate property tax = assessed value * 0.0072
# - Pass values to showPropertyTax function
# - Display formatted currency output
#
# Example:
# Enter the actual value: 100000
# Assessed value: $60,000.00
# Property tax: $432.00
