# Programming Exercise 4-1: Bug Collector
#
# Task: Write a program that collects bug data over 5 days and calculates the total.
#
# Requirements:
# 1. Initialize variables for bugs collected each day and total bugs
bugs = 0
total = 0
# 2. Use a for loop to collect bug data for 5 days
for day in range(5): 
# 3. Ask the user to enter the number of bugs collected each day
    day = int(input("how many bugs did you collect today? "))
# 4. Add each day's bugs to the running total
    total += day 
    print(f"Total bug collected:{total}.")
# 5. Display the total number of bugs collected

# Logic:
# - Use for day in range(5) to loop through 5 days
# - Use += operator to accumulate the total
# - Display the final total after the loop

#
# Example:
# Enter the number of bugs collected today: 5
# Enter the number of bugs collected today: 3
# Enter the number of bugs collected today: 7
# Enter the number of bugs collected today: 2
# Enter the number of bugs collected today: 8
# Total bugs collected: 25
