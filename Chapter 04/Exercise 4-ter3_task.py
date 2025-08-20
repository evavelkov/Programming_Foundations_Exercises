# Programming Exercise 4-ter3: Infinite Loop Examples
#
# Task: Write a program that demonstrates different types of infinite loops.
#
# Requirements:
# 1. Show an example of a commented-out infinite loop using range()
# 2. Show a real infinite loop using itertools.count()
# 3. Import the itertools module
# 4. Demonstrate how to create an infinite loop
#
# Logic:
# - Comment out the range() example (it would take too long)
# - Use from itertools import count
# - Use for i in count(): to create infinite loop
# - Print the value of i in each iteration
#
# Example:
# # Not a real infinite loop
# # for i in range(10**100):
# #   print(i)
#
# # Real infinite loop
# from itertools import count
# for i in count():
#     print("Value of i: ", i)
#
# Note: This will run indefinitely until manually stopped
# The count() function generates numbers 0, 1, 2, 3, ... forever
