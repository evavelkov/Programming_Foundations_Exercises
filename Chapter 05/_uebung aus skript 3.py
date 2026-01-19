

def main(): 
    guthaben = 1000.0
    """Zeigt das Menü"""
    while True: 
        print("\n")
        print(30*"=")
        print("BANKAUTOMAT")
        print(30*"=")
        print("1) Kontostand")
        print("2) Einzahlen")
        print("3) Abheben")
        print("4) Beenden")
        auswahl = input("was möchten sie Wählen (1-4): ")

        if auswahl == "1": 
            konstostand(guthaben)
        elif auswahl == "2": 
            guthaben = einzahlen(guthaben)
        elif auswahl == "3": 
            guthaben = abheben(guthaben)
        elif auswahl == "4": 
            beenden()
            break
        else: 
            print("ungültige Eingabe")
        
def konstostand(guthaben):
    print(f"\nDein aktueller Kontostand liegt ebi {guthaben:.2f}Chf.")
    
def einzahlen(guthaben):
    betrag_einzahlen = float(input("\nWie viel möchten sie einzahlen?: "))
    while betrag_einzahlen <= 0: 
        print("Betrag kann nicht negativ sein.")
        betrag_einzahlen = float(input("\nWie viel möchten sie einzahlen?: "))

    guthaben += betrag_einzahlen
    print("Betrag wurde erfolgreich eingezahlt.")
    print(f"ihr neuer Kontostand lautet {guthaben:.2f}Chf.")
    return guthaben

def abheben(guthaben):
    betrag_abheben = float(input("\nWie viel möchten sie abheben? "))
    while betrag_abheben <= 0: 
        print("Betrag kann nicht negativ sein.")
        betrag_abheben = float(input("\nWie viel möchten sie abheben?: "))

    while betrag_abheben > guthaben: 
        print("Betrag kan nicht grösser als ihr Guthaben sein")
        print(f"Aktuelles Guthaben: {guthaben:.2f}Chf")
        betrag_abheben = float(input("\nWie viel möchten sie abheben? "))

    guthaben -= betrag_abheben
    print("Betrag wurde abgehoben.")
    print(f"ihr neuer Kontostand lautet {guthaben:.2f}Chf.")
    return guthaben

def beenden():
    print(30*"=")
    print("\nAus wiedersehen!")
    print(30*"=")

main()