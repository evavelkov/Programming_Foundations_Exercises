# Programming Exercise 4-9: Ocean Levels
#
# Task: Write a program that calculates and displays the rise in ocean levels over 25 years.
#
# Requirements:
# 1. Initialize a constant for the rise per year (1.8 millimeters)
# 2. Create a table header showing "Year" and "Rise (in millimeters)"
# 3. Use a for loop to calculate the cumulative rise for 25 years
# 4. Display the year number and cumulative rise for each year
# 5. Format the output in a tabular format
#
# Constants:
# - RISE_PER_YEAR = 1.8 millimeters
#
# Logic:
# - Use for year in range(25) to loop through 25 years
# - Add RISE_PER_YEAR to cumulative rise each year
# - Display year + 1 (to show years 1-25 instead of 0-24)
# - Format rise to 2 decimal places
#
# Example output:
# Year		Rise (in millimeters)
# ------------------------------------------
# 1		1.80
# 2		3.60
# 3		5.40
# ... (continues for 25 years)
# 25		45.00
