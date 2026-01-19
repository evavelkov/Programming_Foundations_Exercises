"""Primzahlenrechner zwischen 1 und 100"""

primzahlen = 0 

for zahl in range (2,101):
    ist_primzahl = True

    for teiler in (2, zahl+1):
        if zahl % teiler == 0: 
            ist_primzahl = False
            break 
    if ist_primzahl: 
        print(zahl, end=" ")
        primzahlen += 1

        if primzahlen % 10 == 0: 
            print()
print(f"\ninsgesamt {primzahlen} Primzahlen")

