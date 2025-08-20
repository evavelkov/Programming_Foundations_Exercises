# Programming Exercise 5-6: Stadium Seating Revenue Calculator
#
# Task: Write a program that calculates stadium seating revenue using functions.
#
# Requirements:
# 1. Create a main function that collects seat counts and calculates income
# 2. Create a showIncome function that displays revenue breakdown
# 3. Use global constants for seat prices
# 4. Ask the user to enter counts for three seat classes (A, B, C)
# 5. Calculate income for each class and total revenue
# 6. Display detailed revenue breakdown
#
# Constants:
# - CLASS_A_SEATS = 20 (price per seat)
# - CLASS_B_SEATS = 15 (price per seat)
# - CLASS_C_SEATS = 10 (price per seat)
#
# Functions:
# - main(): collects input, calculates income, calls showIncome()
# - showIncome(incomeAseats, incomeBseats, incomeCseats): displays revenue details
#
# Logic:
# - Get count of each seat class from user
# - Calculate income for each class: count * price
# - Pass income values to showIncome function
# - Calculate total income = sum of all class incomes
# - Display formatted currency output for each class and total
#
# Example:
# Enter count of A seats: 100
# Enter count of B seats: 200
# Enter count of C seats: 300
# Income from class A seats: $ 2,000.00
# Income from class B seats: $ 3,000.00
# Income from class C seats: $ 3,000.00
# Total income: $ 8,000.00
