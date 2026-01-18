"""einmaleins-Tabelle"""

zahl = int(input("Wele einmaleins-Tabelle möchten sie erstellen?: "))

print(f"das kleine Einmaleins für {zahl}:")
print(35*"-")
for i in range(11):    
    loesung = zahl * i
    print(zahl,'x', i, '=', loesung)