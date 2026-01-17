x = float(input("Geben sie eine Zahl ein: "))
y = float(input("Geben sie eine zweite Zahl ein: "))

if x > y: 
    print(f"die Zahle {x} ist die grösste aus der eingabe")
elif y > x: 
    print(f"die Zahl {y} ist die grösste aus der eingabe")
else: 
    print("die beiden Zahlen sind genau gleich")