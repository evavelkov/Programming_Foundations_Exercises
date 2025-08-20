# Programming Exercise 5-17: Prime Number Table
#
# Task: Write a program that displays a table of prime numbers from 1 to 100.
#
# Requirements:
# 1. Create a main function that generates a table of numbers and their prime status
# 2. Create an is_prime function that determines if a number is prime
# 3. Display numbers 1-100 in a table format
# 4. Show whether each number is prime or not prime
#
# Functions:
# - main(): generates table and calls is_prime()
# - is_prime(number): returns True if number is prime, False otherwise
#
# Logic:
# - Use for loop to iterate through numbers 1-100
# - Call is_prime function for each number
# - Check divisibility from 2 to half the number
# - Display formatted table with number and prime status
#
# Example output:
# number 	 is prime
# ------------------------
# 1 	 not prime
# 2 	 prime
# 3 	 prime
# 4 	 not prime
# 5 	 prime
# ... (continues for all 100 numbers)
#
# Note: The table will show all numbers from 1 to 100 with their prime status
