# Programming Exercise 5-16: Prime Number Checker
#
# Task: Write a program that determines if a number is prime using functions.
#
# Requirements:
# 1. Create a main function that handles user input and calls prime checking function
# 2. Create an is_prime function that determines if a number is prime
# 3. Ask the user to enter an integer
# 4. Display whether the number is prime or not
#
# Functions:
# - main(): handles input and calls is_prime()
# - is_prime(number): returns True if number is prime, False otherwise
#
# Logic:
# - Get integer from user
# - Pass number to is_prime function
# - Check divisibility from 2 to half the number
# - Use modulo operator (%) to check for remainders
# - Return True if no divisors found, False otherwise
# - Display appropriate message based on result
#
# Example:
# Enter an integer: 17
# The number you entered is a prime number.
#
# Enter an integer: 24
# The number you entered is not a prime number.
