# Programming Exercise 4-3: Lap Time Tracker
#
# Task: Write a program that tracks lap times and calculates fastest, slowest, and average times.
#
# Requirements:
# 1. Ask the user to enter the number of laps
# 2. Use a for loop to collect lap times for each lap
# 3. Track the fastest lap time (lowest value)
# 4. Track the slowest lap time (highest value)
# 5. Calculate the total time for all laps
# 6. Calculate and display the average lap time
# 7. Display fastest, slowest, and average lap times
#
# Logic:
# - Initialize fastest and slowest as None
# - Use for lap in range(1, laps + 1) to loop through laps
# - Compare each lap time to current fastest/slowest
# - Use running total to calculate average
# - Use round() function to format average to 2 decimal places
#
# Example:
# Enter number of laps: 3
# 
# Lap 1 of 3
# Enter lap time: 45.2
# 
# Lap 2 of 3
# Enter lap time: 42.8
# 
# Lap 3 of 3
# Enter lap time: 47.1
# 
# Fastest Lap Time: 42.8
# Slowest Lap Time: 47.1
# Average Lap Time: 45.03
