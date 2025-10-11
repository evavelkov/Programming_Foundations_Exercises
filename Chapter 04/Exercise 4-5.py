# Programming Exercise 4-5: Rainfall Statistics
#
# Task: Write a program that collects rainfall data and calculates statistics.
#
# Requirements:
# 1. Ask the user to enter the number of years

montnames = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", 
             "August", "September", "Oktober", "November", "Dezember"]
#liste mit namen immer in [] setzten und mit "" und , trennen 
totalmonth = 0
totalrain = 0
years = int(input("How many years: "))
# 2. Use nested for loops to collect rainfall data:
#    - Outer loop: iterate through each year
for year in range(years):
    print(f"in year {year + 1}: ")
    for month in montnames: #wenn es aus eine Liste nimmt, braucht es kein "in range()" !
       monthrainfall = float(input(f"enter rainfall for month {month}: ")) #month nimmt jedes "" einzeln da es in range of montnames ist
       totalmonth += 1
       totalrain += monthrainfall

average = totalrain / totalmonth

print(f"for {totalmonth} months")
print(f"for rainfall: {totalrain:.2f} inch")
print(f"average monthy rainfall: {average:.2f} inch")

#       - Inner loop: iterate through each month (12 months per year)
        #add to total number of months
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
