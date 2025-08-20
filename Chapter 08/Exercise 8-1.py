# Programming Exercise 8-1: Name Formatting
#
# Task: Write a program that formats a person's name in different ways.
#
# Requirements:
# 1. Create a main function that handles user input and name formatting
# 2. Get first name and last name from user input
# 3. Display initials (first letter of each name with periods)
# 4. Display name in address book format (first initial + rest of first name + last name in caps)
# 5. Display username (first initial + last name, all lowercase)
#
# Functions:
# - main(): handles user input and displays formatted names
#
# Logic:
# - Get first name from user input
# - Get last name from user input
# - Display initials: first letter of each name with periods
# - Display address book format: first initial + rest of first name + space + last name in caps
# - Display username: first initial + last name, all lowercase
#
# String Operations:
# - string[0] - get first character
# - string[1:] - get rest of string (from index 1 to end)
# - string.upper() - convert to uppercase
# - string.lower() - convert to lowercase
#
# Output Format:
# - Initials: [F].[L]. (with periods)
# - Address Book: [F][irstname] [LASTNAME]
# - Username: [f][lastname] (all lowercase)
#
# Example:
# Enter your first name: John
# Enter your last name: Smith
#
# Initials: J.S.
# Name in Address Book: John SMITH
# Username: jsmith
#
# Note: 
# - Program handles any first and last names
# - Uses string slicing and case conversion methods
# - Displays three different name formats
