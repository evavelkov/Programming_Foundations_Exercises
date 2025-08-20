# Programming Exercise 4-10: Tuition Increase
#
# Task: Write a program that calculates projected tuition increases over 5 years.
#
# Requirements:
# 1. Initialize constants for the increase rate and starting tuition amount
# 2. Create a table header showing "Year" and "Projected Tuition (per Semester)"
# 3. Use a for loop to calculate tuition for 5 years
# 4. Apply a 3% increase each year to the previous year's tuition
# 5. Display the projected tuition for each year
#
# Constants:
# - INCREASE_PER_YEAR = 0.03 (3% increase)
# - STARTING_AMOUNT = 8000.0 (starting tuition)
#
# Logic:
# - Use for year in range(5) to loop through 5 years
# - Calculate new tuition = previous tuition + (previous tuition * 0.03)
# - Display year + 1 and formatted tuition amount
# - Format tuition with commas and 2 decimal places
#
# Example output:
# Year	 Projected Tuition (per Semester)
# ------------------------------------------
# 1	$8,240.00
# 2	$8,487.20
# 3	$8,741.82
# 4	$9,004.07
# 5	$9,274.19
