# Programming Exercise 4-6: Miles to Kilometers Converter
#
# Task: Write a program that converts miles to kilometers and displays a conversion table.
miles = 0

conversion = 1.60934
# Requirements:
# 1. Create a table header showing "Miles" and "Kilometers"
# 2. Use a for loop to convert miles to kilometers
# 3. Display miles from 10 to 80 in increments of 10
# 4. Calculate kilometers for each mile value
# 5. Display the results in a tabular format
print("Miles\tKilometers")
print("-"*25)

for miles in range(10, 81, 10):
    kilometers = round(miles * conversion, 2)
    print(miles, "\t", kilometers)
# Logic:
# - Use for miles in range(10, 81, 10) to get 10, 20, 30, 40, 50, 60, 70, 80
# - Calculate kilometers = miles * 1.60934
# - Use round() function to format kilometers to 2 decimal places
# - Display each row with miles and kilometers
#
# Conversion factor: 1 mile = 1.60934 kilometers
#
# Example output:
# Miles	Kilometers
# ------------------
# 10	16.09
# 20	32.19
# 30	48.28
# 40	64.37
# 50	80.47
# 60	96.56
# 70	112.65
# 80	128.75
