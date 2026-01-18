"""verwendung walrus-operator"""

summe = 0 

print("Geben sie eine Zahl ein (oder -1 zum beenden)")

while (zahl := float(input("Zahl: "))) != -1: #solange Zahlen eingeben, bis -1 gewählt wird
    summe += zahl #summiert alle eingegebenen Zahlen auf 
print(f"die Summe ist: {summe}")