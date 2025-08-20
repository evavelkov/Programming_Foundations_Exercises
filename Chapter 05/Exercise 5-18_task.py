# Programming Exercise 5-18: Loan Payment Calculator
#
# Task: Write a program that calculates monthly loan payments using functions.
#
# Requirements:
# 1. Create a main function that collects loan information and displays results
# 2. Create a calculate_payment function that computes monthly payment amount
# 3. Ask the user to enter loan amount, interest rate, and number of months
# 4. Calculate and display the monthly payment amount
#
# Functions:
# - main(): collects input, calls calculate_payment(), displays results
# - calculate_payment(A, R, M): calculates monthly payment amount
#
# Loan Payment Formula:
# - Monthly Payment = (R × A) / (1 - (1 + R)^(-M))
# - Where: A = loan amount, R = monthly interest rate (as decimal), M = number of months
#
# Logic:
# - Get loan amount, interest rate percentage, and number of months
# - Convert interest rate from percentage to decimal (divide by 100)
# - Use loan payment formula to calculate monthly payment
# - Display formatted results with currency formatting
#
# Example:
# Enter the loan amount: 10000
# Enter the monthly interest rate as a percentage: 5
# Enter the number of months: 12
# 
# Loan Amount: $10,000.00
# Monthly Interest: 5.00%
# Payment Months: 12
# 
# Monthly Payment Amount: $856.07
