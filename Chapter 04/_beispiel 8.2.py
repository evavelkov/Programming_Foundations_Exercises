print("Kleines Einmaleins:") 
print() #neue Zeile
for i in range(1, 11):
    for j in range(1, 11): 
        produkt = i * j
        print(f"{produkt:4}", end="")
    print() # Neue Zeile nach jeder Reihe


hoehe = int(input("Hoehe des Rechtecks: "))
breite = int(input("Breite des Rechtecks: "))
for zeile in range(hoehe):
    for spalte in range(breite): 
        print("*", end="")
    print() # Neue Zeile