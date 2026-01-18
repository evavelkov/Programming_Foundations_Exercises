"""erstellt ein Dreieck aus Sternen (*)"""

hohe = int(input("Geben die die Höhe des Dreiecks an: ")) #z.B. 5

for zeile in range(1, hohe + 1): #+1 weil es sonst nur 4 wäre
    for spalte in range(zeile): 
        print("*", end=" ")
    print()