# Programming Exercise 5-3: Insurance Calculator
#
# Task: Write a program that calculates minimum insurance coverage using functions.
#
# Requirements:
# 1. Create a main function that handles user input and calculations
# 2. Create a showInsure function that displays insurance information
# 3. Use a global constant for the replacement percentage
# 4. Ask the user to enter the replacement cost
# 5. Calculate minimum insurance as 80% of replacement cost
# 6. Display detailed insurance information
#
# Constants:
REPLACE_PERCENT = 0.8
#
# Functions:
# - main(): handles input, calculates insurance, calls showInsure()
# - showInsure(replace, minInsure): displays insurance details
def main(): 
    replace = 0.0
    minInsurance = 0.0
    replace = float(input("Input replacement cost: "))

    minInsurance = replace * REPLACE_PERCENT
    showInsureance(replace, minInsurance)


def showInsureance(replace, minInsurance):
    print(f"replacement amount: ${replace:.2f}")
    print(f"Percent insured: {REPLACE_PERCENT*100:.2f}%")
    print(f"minimum insurance: {minInsurance:.2f}")


main()
# Logic:
# - Get replacement cost from user
# - Calculate minimum insurance = replacement cost * 0.8
# - Pass both values to showInsure function
# - Display formatted output with currency and percentage formatting
#
# Example:
# Enter the replacement amount: 100000
# Replacement cost: $100,000.00
# Percent insured: 80.00%
# Minimum insurance: $80,000.00
