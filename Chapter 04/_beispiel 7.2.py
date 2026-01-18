zahl = int(input("Geben Sie eine Zahl ein: "))

if zahl < 2:
    print(f"{zahl} ist keine Primzahl.") 
else:
 # Suche nach einem Teiler
    for teiler in range(2, zahl):
        if zahl % teiler == 0:
 # Teiler gefunden!
            print(f"{zahl} ist keine Primzahl.")
            print(f"Sie ist teilbar durch {teiler}.") 
            break
    else:
 # Kein Teiler gefunden (break wurde nie ausgefuehrt) 
        print(f"{zahl} ist eine Primzahl!")