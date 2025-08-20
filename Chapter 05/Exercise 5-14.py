# Programming Exercise 5-14: Grade Calculator with Functions
#
# Task: Write a program that calculates grades and averages using multiple functions.
#
# Requirements:
# 1. Create a main function that collects 5 test scores
# 2. Create a calc_average function that calculates the average of 5 scores
# 3. Create a determine_grade function that converts numeric scores to letter grades
# 4. Display a table showing each score with its letter grade
# 5. Show the average score and its letter grade
#
# Functions:
# - main(): collects input, calls other functions, displays results
# - calc_average(s1, s2, s3, s4, s5): returns average of 5 scores
# - determine_grade(score): returns letter grade based on numeric score
#
# Grade Scale:
# - 90-100: A
# - 80-89: B
# - 70-79: C
# - 60-69: D
# - Below 60: F
#
# Logic:
# - Get 5 test scores from user
# - Calculate average using calc_average function
# - Use determine_grade function for each score and average
# - Display formatted table with scores, numeric grades, and letter grades
#
# Example:
# Enter score 1: 85
# Enter score 2: 92
# Enter score 3: 78
# Enter score 4: 95
# Enter score 5: 88
# Score		Numeric Grade	Letter Grade
# ----------------------------------------------------
# score 1:	85.0		B
# score 2:	92.0		A
# score 3:	78.0		C
# score 4:	95.0		A
# score 5:	88.0		B
# Average score:	87.6		B
