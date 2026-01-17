"""Taschenrechner"""
x = None
y = None 
operator = None
#eingabe:
if x is None: 
    x = float(input("Erste Zahl eingeben: "))

operator = input("geben sie einen Operator ein (+,-,*,/): ")

if y is None:
    y = float(input("Zweite Zhal eingeben: "))

if operator == '+':
    addition = x + y 
    print(f"die lösung ist {addition}")
elif operator == '-':
    subraction = x - y 
    print(f"die lösung ist {subraction}")
elif operator == '*':
    multipication = x * y
    print(f"die lösung ist {multipication}")
elif operator == '/':
    if y == 0:
        print("division durch 0 ist nicht möglich.")
    else:
        division = x / y
        print(f"die lösung ist {division}")
else: 
    print("ungültige Eingabe")


