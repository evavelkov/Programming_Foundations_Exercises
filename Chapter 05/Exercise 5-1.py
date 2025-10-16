# Programming Exercise 5-1: Kilometer to Miles Converter
#
# Task: Write a program that converts kilometers to miles using functions.
#
# Requirements:
# 1. Create a main function that handles user input and calls other functions
# 2. Create a showMiles function that performs the conversion and displays results
# 3. Use a global constant for the conversion factor
# 4. Ask the user to enter a distance in kilometers
# 5. Convert kilometers to miles and display the result
#
# Constants:
# - KILOMETERS_TO_MILES = 0.6214

# Functions:
# - main(): handles input and calls showMiles()
# - showMiles(kilometers): performs conversion and displays result

KILOMETERS_TO_MILES = 0.6214
def main():
    mykilometers = 0 
    mykilometers = float(input("Enter disntance in kilometers: "))
    kmrechner(mykilometers) #ruft die nächste funktion auf und nimmt die var
                            #welche eingegeben wurde in dieser funktion


def kmrechner(mykilometers):
    mymiles = 0
    mymiles = KILOMETERS_TO_MILES * mykilometers
    print(f"your distance in miles is {mymiles:.2f}")

main() #call main
# Logic:
# - Get input in main function
# - Pass kilometers to showMiles function
# - Calculate miles = kilometers * KILOMETERS_TO_MILES
# - Display formatted output with 2 decimal places
# Example:
# Enter the distance in kilometers: 10
# The conversion of 10.00 kilometers
# to miles is 6.21 miles.