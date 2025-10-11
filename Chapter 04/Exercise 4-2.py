# Programming Exercise 4-2: Calories Burned
#
# Task: Write a program that displays calories burned during exercise over time.
#
# Requirements:
# 1. Initialize a constant for calories burned per minute (4.2)
calpermin = 4.2
# 2. Create a table header showing "Minutes" and "Calories Burned"
minutes = 0 
calburned = 0 
# 3. Use a for loop to calculate calories burned for different time periods
print("-"*40)
print("minutes\t\tcalories burned")
# 4. Display minutes from 10 to 30 in increments of 5
for minutes in range(10, 31, 5):
    calburned = calpermin * minutes
    print(minutes, "\t\t", calburned)
# 5. Calculate calories burned for each time period
# 6. Display the results in a tabular format
#
# Constants:
# - caloriesPerMinute = 4.2
#
# Logic:
# - Use for minutes in range(10, 31, 5) to get 10, 15, 20, 25, 30
# - Calculate caloriesBurned = caloriesPerMinute * minutes
# - Display each row with minutes and calories burned
#
# Example output:
# Minutes		Calories Burned
# -------------------------------
# 10		42.0
# 15		63.0
# 20		84.0
# 25		105.0
# 30		126.0
