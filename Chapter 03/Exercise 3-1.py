# Programming Exercise 3-1: Number Classification
#
# Task: Write a program that classifies a number based on its properties.
#
# Requirements:
# 1. Ask the user to enter an integer
number = int(input("Enter an interger: "))
# 2. Determine if the number is positive, negative, or zero
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number number is zero.")
# 3. Determine if the number is even or odd
if number % 2 == 0:
    print("your number is even.")
else:
    print("you number is odd.")


# 4. Display both classifications
#
# Logic:
# - For positive/negative/zero: use if-elif-else with comparison operators
# - For even/odd: use modulo operator (%) to check remainder when divided by 2
#
# Example:
# Enter an integer: 7
# Positive
# Odd
#
# Enter an integer: -4
# Negative
# Even
#
# Enter an integer: 0
# Zero
# Even
