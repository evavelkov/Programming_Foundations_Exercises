# Programming Exercise 7-15: Weekly Gas Prices Line Graph
#
# Task: Write a program that creates a line graph from weekly gas price data.
#
# Requirements:
# 1. Import matplotlib.pyplot module
# 2. Create a main function that handles file reading and graph creation
# 3. Read gas price data from '1994_Weekly_Gas_Averages.txt' file
# 4. Create x-coordinates for weeks (1-52)
# 5. Create a line graph with proper formatting
# 6. Add title, labels, and axis limits
# 7. Display the graph
#
# Functions:
# - main(): handles file operations and graph creation
#
# Constants:
# - NUM_WEEKS = 52
#
# Logic:
# - Open '1994_Weekly_Gas_Averages.txt' file using with statement
# - Read all lines from file into a list
# - Strip newline characters from each gas price
# - Create x-coordinates list (weeks 1-52)
# - Create line graph using plt.plot()
# - Set x-axis limits (1 to 52)
# - Add title and axis labels
# - Display the graph using plt.show()
#
# File Operations:
# - with open('1994_Weekly_Gas_Averages.txt', 'r') as gas_file: - opens file for reading
# - gas_file.readlines() - reads all lines into list
# - line.rstrip('\n') - removes newline characters
#
# Graph Creation:
# - plt.plot(x_coords, gas) - creates line graph
# - plt.xlim(xmin=1, xmax=NUM_WEEKS) - sets x-axis limits
# - plt.title('1994 Weekly Gas Prices') - adds chart title
# - plt.xlabel('Weeks (by number)') - adds x-axis label
# - plt.ylabel('Average Prices') - adds y-axis label
# - plt.show() - displays the graph
#
# Example:
# (Displays line graph showing gas price trends over 52 weeks)
#
# Note: 
# - Program assumes '1994_Weekly_Gas_Averages.txt' exists with one price per line
# - Requires matplotlib library to be installed
# - Creates visual representation of gas price trends
# - Uses with statement for automatic file closing
# - Displays interactive graph window
# - Shows 52 weeks of data with proper axis formatting
