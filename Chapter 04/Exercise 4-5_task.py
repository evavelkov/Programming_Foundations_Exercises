# Programming Exercise 4-5: Rainfall Statistics
#
# Task: Write a program that collects rainfall data and calculates statistics.
#
# Requirements:
# 1. Ask the user to enter the number of years
# 2. Use nested for loops to collect rainfall data:
#    - Outer loop: iterate through each year
#    - Inner loop: iterate through each month (12 months per year)
# 3. Ask the user to enter rainfall amount for each month
# 4. Calculate the total rainfall for all months
# 5. Calculate the average monthly rainfall
# 6. Display the total months, total rainfall, and average rainfall
#
# Logic:
# - Use nested loops: for year in range(years) and for month in range(12)
# - Keep running totals for totalRainfall and totalMonths
# - Calculate average = totalRainfall / totalMonths
# - Format output with commas and 2 decimal places
#
# Example:
# Enter the number of years: 2
# For year 1:
# Enter the rainfall amount for the month: 3.2
# Enter the rainfall amount for the month: 2.8
# ... (continue for all 12 months)
# For year 2:
# Enter the rainfall amount for the month: 4.1
# ... (continue for all 12 months)
# For 24 months
# Total rainfall: 85.60 inches
# Average monthly rainfall: 3.57 inches
