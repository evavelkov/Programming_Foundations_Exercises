# Programming Exercise 3-2: Area Comparison
#
# Task: Write a program that compares the areas of two rectangles.
#
# Requirements:
# 1. Ask the user to enter the length and width of rectangle A
length_a = float(input("Lenght of A: "))
width_a = float(input("Width of A: "))
# 2. Ask the user to enter the length and width of rectangle B
length_b = float(input("Lenght of B: "))
width_b = float(input("Width of B: "))
# 3. Calculate the area of both rectangles
area_a = length_a * width_a
area_b = length_b * width_b
# 4. Display both areas formatted to 2 decimal places
print(f"Area A = {area_a:.2f}m2.")
print(f"Area B = {area_b:.2f}m2.")
# 5. Compare the areas and display which one is greater, or if they are equal
if area_a > area_b:
    print("Area A is greater than Area B.")
elif area_b > area_a:
    print("Area B is greater tna Area A.")
else:
    print("the Areas are equal.")
#
# Formula: area = length * width
#
# Logic for comparison:
# - Use if-elif-else to compare areaA and areaB
# - Display appropriate message based on comparison
#
# Example:
# Enter length A: 10
# Enter width A: 5
# Enter length B: 8
# Enter width B: 6
# Area A: 50.00
# Area B: 48.00
# Area A is greater than Area B.
