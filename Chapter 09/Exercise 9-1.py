# Programming Exercise 9-1: Galilean Moon Information Lookup
#
# Task: Write a program that provides information about the Galilean moons of Jupiter.
#
# Requirements:
# 1. Create a main function that handles user input and moon information lookup
# 2. Create dictionaries to store moon data (mean radius, surface gravity, orbital period)
# 3. Get moon name from user input
# 4. Look up and display information for the specified moon
# 5. Handle invalid moon names with appropriate error message
#
# Functions:
# - main(): handles user input and moon information lookup
#
# Logic:
# - Initialize three dictionaries with moon data:
#   - mean_radius: stores mean radius in km for each moon
#   - surface_gravity: stores surface gravity in m/s² for each moon
#   - orbital_period: stores orbital period in days for each moon
# - Get moon name from user input
# - Convert moon name to lowercase for case-insensitive matching
# - Check if moon name exists in dictionaries using 'in' operator
# - If moon exists: display all three pieces of information
# - If moon doesn't exist: display error message
#
# Moon Data:
# - Io: radius 1821.6 km, gravity 1.796 m/s², period 1.769 days
# - Europa: radius 1560.8 km, gravity 1.314 m/s², period 3.551 days
# - Ganymede: radius 2634.1 km, gravity 1.428 m/s², period 7.154 days
# - Callisto: radius 2410.3 km, gravity 1.235 m/s², period 16.689 days
#
# Dictionary Operations:
# - dictionary[key] - access value for key
# - key in dictionary - check if key exists
# - string.lower() - convert to lowercase
# - string.title() - convert to title case
#
# Example:
# Enter name of Galilean moon of Jupiter: io
# Details of Io are:
# Mean Radius: 1821.6 km
# Surface Gravity: 1.796 m/s²
# Orbital Period: 1.769 days
#
# Note: 
# - Program handles case-insensitive input
# - Uses multiple dictionaries to store different types of data
# - Provides clear error message for invalid moon names
# - Displays information in formatted output
