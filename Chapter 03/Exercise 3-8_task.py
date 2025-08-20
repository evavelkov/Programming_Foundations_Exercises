# Programming Exercise 3-8: Hot Dog Cookout Calculator
#
# Task: Write a program that calculates the number of hot dog and bun packages needed for a cookout.
#
# Requirements:
# 1. Ask the user to enter the number of people attending the cookout
# 2. Ask the user to enter the number of hot dogs per person
# 3. Calculate the total number of hot dogs and buns needed
# 4. Calculate the minimum packages needed:
#    - Hot dogs come in packages of 10
#    - Buns come in packages of 8
# 5. Calculate leftovers for both hot dogs and buns
# 6. Display all results
#
# Constants:
# - HOT_DOGS_PER_PACKAGE = 10
# - BUNS_PER_PACKAGE = 8
#
# Logic:
# - Calculate total needed = people * hot dogs per person
# - Calculate packages needed using integer division (//)
# - Add extra package if there are leftovers (using modulo %)
# - Calculate final leftovers after purchasing packages
#
# Example:
# Enter the number of people attending the cookout: 25
# Enter the number of hot dogs for each person: 2
# Minimum packages of hot dogs needed: 5
# Minimum packages of hot dog buns needed: 7
# Hot dogs left over: 0
# Hot dog buns left over: 6
