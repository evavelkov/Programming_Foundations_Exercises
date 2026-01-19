"""Bankautomat-Simulator"""

print("\n=== BANKAUTOMAT-SIMULATOR ===")

guthaben = 1000.0

while True: 
    print("\nMENÜ")
    print("1) Kontostand")
    print("2) Einzahlen")
    print("3) Abheben")
    print("4) Beenden")

    wahl = input("Eingabe Wahl: \n")

    if wahl == "1": 
        print(f"\nIhr aktueller Kontostand ist: {guthaben:.2f}Chf")
    
    elif wahl == "2": 
        #Einzahlen
        einzahlen = float(input("\nBetrag einzahlen: "))
        if einzahlen <= 0: 
            print("Betrag kann nicht negativ sein!")
        else: 
            guthaben += einzahlen
            print("Betrag wurde erfolgreich eingezahlt.")
            print(f"Ihr neuer Kontostand ist {guthaben:.2f}Chf")

    elif wahl == "3":
        #Abheben
        abheben = float(input("\nwie viel möchten sie abheben?: "))
        if abheben <= 0: 
            print("Betrag muss positiv sein")
        elif abheben > guthaben: 
            print("sie können nicht mehr als ihr Guthaben abheben!")
            print(f"Verfügbares Guthaben: {guthaben:.2f}Chf")
        else: 
            guthaben -= abheben
            print("Betrag wurde erfolgreich abgehoben")
            print(f"Ihr neuer Kontostand ist {guthaben:.2f}Chf")

    elif wahl == "4":
        print("\nEinen schönen Tag!") 
        break

    else: 
        print("\nUnghültige Auswahl. bitte wählen sie zwischen 1-4.")