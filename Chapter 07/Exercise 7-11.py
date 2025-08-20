# Programming Exercise 7-11: Lo Shu Magic Square Validator
#
# Task: Write a program that validates if a 3x3 grid is a Lo Shu Magic Square.
#
# Requirements:
# 1. Define global constants for grid dimensions and value ranges
# 2. Create a main function that tests a predefined magic square
# 3. Create multiple functions to check different magic square properties
# 4. Display the grid and validation result
# 5. Implement comprehensive validation logic
#
# Functions:
# - main(): handles display and calls validation functions
# - display_square_list(value_list): displays 3x3 grid
# - is_magic_square(value_list): main validation function
# - check_range(value_list): validates value range (1-9)
# - check_unique(value_list): validates all values are unique
# - check_row_sum(value_list): validates row sums are equal
# - check_col_sum(value_list): validates column sums are equal
# - check_diag_sum(value_list): validates diagonal sums are equal
#
# Constants:
# - ROWS = 3, COLS = 3
# - MIN = 1, MAX = 9
#
# Logic:
# - Define test 3x3 grid
# - Display grid using nested loops
# - Call is_magic_square() for validation
# - Display validation result
# - In validation functions:
#   - Check range: all values 1-9
#   - Check unique: no duplicate values
#   - Check rows: all row sums equal
#   - Check columns: all column sums equal
#   - Check diagonals: both diagonal sums equal
#
# Magic Square Properties:
# - All values must be 1-9
# - All values must be unique
# - Row sums must be equal
# - Column sums must be equal
# - Diagonal sums must be equal
#
# Output Format:
# - Display 3x3 grid
# - Validation result: 'This is a Lo Shu magic square.' or 'This is not a Lo Shu magic square.'
#
# Example:
# 4 9 2
# 3 5 7
# 8 1 6
# This is a Lo Shu magic square.
#
# Note: 
# - Lo Shu Magic Square is a 3x3 grid with specific properties
# - All rows, columns, and diagonals must sum to the same value
# - Uses comprehensive validation with multiple functions
# - Tests predefined magic square example
