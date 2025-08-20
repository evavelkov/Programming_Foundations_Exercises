# Programming Exercise 5-15: Odd/Even Counter
#
# Task: Write a program that counts odd and even numbers using functions.
#
# Requirements:
# 1. Import the random module
# 2. Create a main function that generates random numbers and counts them
# 3. Create an isEven function that determines if a number is even
# 4. Generate 100 random numbers between 1 and 1000
# 5. Count how many are odd and how many are even
# 6. Display the results
#
# Functions:
# - main(): generates random numbers and counts odd/even
# - isEven(number): returns True if number is even, False if odd
#
# Logic:
# - Use for loop to generate 100 random numbers
# - Use random.randint(1, 1000) to generate each number
# - Call isEven function to check each number
# - Use modulo operator (%) to determine if number is even
# - Keep counters for odd and even numbers
# - Display final count results
#
# Example:
# Out of 100 random numbers, 47 were odd, and 53 were even.
#
# Note: Results will vary due to random number generation
