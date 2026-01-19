#zahlenliste verarbeiten 
#benutzer soll 10 Zahlen eingeben
#die summe diese 10 zahlen berechnen 
#den durchschnitt berechnen 
#die grösste und kleinste Zhal finden 

def main():
    liste = eingabe()
    summe_ergebnis = summe(liste)
    print("finish")

def eingabe():
    liste = []
    zahl = 0
    # for zahl in range(1,11):
    while len(liste) != 10:
        zahl += 1
        eingabe = input(f"Geben sie ihre {zahl}. Zahl ein: ")
        liste.append(int(eingabe)) #muss int sein, da man sonst nicht rechnen kann
    return liste 

def summe(): 
    pass

def durchschnitt(): 
    pass

def min_max():
    pass

if __name__ == '__main__':
    main()