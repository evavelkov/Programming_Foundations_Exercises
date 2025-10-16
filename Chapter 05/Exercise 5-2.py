# Programming Exercise 5-2: String Repeater Function
#
# Task: Write a program that creates a function to repeat text a specified number of times.
#
# Requirements:
# 1. Create a main function that tests the repeat function
def main():
    print(repeat('hi',10))

# 2. Create a repeat function that takes text and multiplier as parameters
def repeat(text,multiplier):
    output = '' # - Initialize output as empty string
    output = text * multiplier
    print(main)

main()
# 3. The repeat function should return a string with text repeated multiplier times
# 4. Test the function with sample input

# Functions:
# - main(): calls repeat function and prints result
# - repeat(text, multiplier): returns text repeated multiplier times
#
# Logic:

# - Use string multiplication: output = text * multiplier
# - Return the repeated string
# - Test with 'Hi' repeated 3 times
#
# Example:
# HiHiHi
#
# Note: The function should work with any text and any positive integer multiplier
