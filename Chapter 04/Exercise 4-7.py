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
dayPennies = 1
total = 0.0
NumDays = int(input("How may days would you like to eneter?: "))
# - Use for day in range(1, numDays + 1) to loop through days
print("Day\tPennies ")
print("-"*30)
for day in range(1, NumDays + 1):
    print(f"{day}\t${dayPennies / 100:.2f}") #/ 100:.2f wird wuche gerechnet und auf 2 KOmmastellen weil sonst druck es ein Dollar
    
    total += dayPennies #total muss als erst inizialisiert werden da sonst vorher alles *2 gerechnet wird 
    dayPennies *= 2 #*2 erst nach dem Total rechnen da es sonst das Total *2 rechnet und somit falsch ist

# - Display each day's salary in dollars (pennies / 100)
# - Double the pennies each day: dayPennies *= 2
# - Keep running total of all pennies
print(f"The total salary for {NumDays} is: ${total / 100:.2f}")
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
