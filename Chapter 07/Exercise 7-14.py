# Programming Exercise 7-14: Monthly Expenses Pie Chart
#
# Task: Write a program that creates a pie chart from monthly expense data.
#
# Requirements:
# 1. Import matplotlib.pyplot module
# 2. Create a main function that handles file reading and chart creation
# 3. Read expense data from 'expenses.txt' file
# 4. Define slice labels for different expense categories
# 5. Create a pie chart with the expense data
# 6. Add title and display the chart
#
# Functions:
# - main(): handles file operations and chart creation
#
# Logic:
# - Open 'expenses.txt' file using with statement
# - Read all lines from file into a list
# - Strip newline characters from each expense value
# - Define slice labels for expense categories
# - Create pie chart using plt.pie()
# - Add title to the chart
# - Display the chart using plt.show()
#
# File Operations:
# - with open('expenses.txt', 'r') as expense_file: - opens file for reading
# - expense_file.readlines() - reads all lines into list
# - line.rstrip('\n') - removes newline characters
#
# Chart Creation:
# - plt.pie(expenses, labels=slice_labels) - creates pie chart
# - plt.title('Monthly Expenses') - adds chart title
# - plt.show() - displays the chart
#
# Slice Labels:
# - ['Rent', 'Gas', 'Food', 'Clothing', 'Car Payment', 'Misc']
#
# Example:
# (Displays pie chart with 6 slices showing expense distribution)
#
# Note: 
# - Program assumes 'expenses.txt' exists with one expense amount per line
# - Requires matplotlib library to be installed
# - Creates visual representation of expense data
# - Uses with statement for automatic file closing
# - Displays interactive chart window
