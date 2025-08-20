# Programming Exercise 4-7: Pennies for Pay
#
# Task: Write a program that calculates salary based on doubling pennies each day.
#
# Requirements:
# 1. Ask the user to enter the number of days
# 2. Start with 1 penny on day 1
# 3. Double the pennies each day (1, 2, 4, 8, 16, etc.)
# 4. Display a table showing the salary for each day
# 5. Calculate and display the total salary for all days
#
# Logic:
# - Initialize dayPennies = 1 (starting with 1 penny)
# - Use for day in range(1, numDays + 1) to loop through days
# - Display each day's salary in dollars (pennies / 100)
# - Double the pennies each day: dayPennies *= 2
# - Keep running total of all pennies
# - Convert total to dollars for final display
#
# Example:
# Enter the number of days: 5
# Day	Pennies
# -------------------------
# 1	$0.01
# 2	$0.02
# 3	$0.04
# 4	$0.08
# 5	$0.16
# The total salary for 5 days is: $0.31
