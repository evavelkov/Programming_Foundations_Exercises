#Funktion welche celsius akzeptiert und in Fahrenheit zurückgibt 
#Formel umrechnung:
#F = C * (9/5) + 32

def celsius_nach_fahrenheit():
    c = float(input("Geben sie Grad Celsius ein: "))
    f = c * (9/5) + 32
    return f,c

f, c = celsius_nach_fahrenheit()
print(f"{c}°C ist {f}°F.")
