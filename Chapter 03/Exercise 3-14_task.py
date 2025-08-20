# Programming Exercise 3-14: Time Calculator
#
# Task: Write a program that converts seconds into days, hours, minutes, and seconds.
#
# Requirements:
# 1. Ask the user to enter the number of seconds
# 2. Calculate the equivalent time units:
#    - Days: seconds // 86400 (24 * 60 * 60)
#    - Hours: seconds // 3600 (60 * 60)
#    - Minutes: seconds // 60
#    - Remaining seconds: use modulo operator (%)
# 3. Display the results in a user-friendly format
# 4. Handle special case: if less than one minute, display appropriate message
#
# Constants:
# - 86400 seconds = 1 day
# - 3600 seconds = 1 hour
# - 60 seconds = 1 minute
#
# Example:
# Enter the number of seconds: 3661
# 3661 seconds are equal to:
# 61 full minute(s) and 1 seconds.
# 1 full hour(s) and 61 seconds.
#
# Enter the number of seconds: 30
# The number of seconds is less than one minute.
