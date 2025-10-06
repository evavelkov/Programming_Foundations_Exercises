
zahl = int(input("geben sie eine zahl ein: "))
print(f"das kleine Einmaleins für {zahl}: ")
print("-"*40)
for i in range(1, 11):
    ergebnis = zahl * i
    print(f"{zahl} x {i} = {ergebnis}")
