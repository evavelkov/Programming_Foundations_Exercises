anfangssaldo = 0 
def main():
    """diese funktion heisst den benutzer wilkommen"""
    print("Wilkommen Benutzer!")
    anfangssaldo = float(input("Bitte geben sie ihren aktuellen Kontrostand ein: "))
    print("wählen sie ihre Option aus:")
    eingabe_user()

def eingabe_user():
    while True:
        hauptmenu ()
        wahl = int(input("Wählen sie bitte eine option aus: "))
        if wahl == 1:
            option_1()
        elif wahl == 2:
            option_2()
        elif wahl == 3:
            option_3()
        elif wahl == 4:
            print("Programm wird beendet!")
            break
        else:
            print("Eingabe ungültig!")
            #braucht es weil sonst läuft das programm in einer endlosschleife

def hauptmenu():
    """diese funktion zeigt das hauptmenü an"""
    print("\n===== HAUPTMENÜ =====")
    print("Option 1: Kontostand")
    print("Option 2: Geld Einzahlen")
    print("Option 3: Geld abheben")
    print("Option 4: Beenden")
    print("="*21)

def option_1():
    print("\n ==== KONTOSTANDT ====")

def option_2():
    print("\n ==== GELD EINZAHLEN ====")

def option_3(): 
    print("\n ==== GELD ABHEBEN ====")
    auszug = float(input("Wie viel möchten sie abheben? "))
    if auszug < anfangssaldo:
        print("Auszug erfolgreich")
    else:
        print("auszug nicht möglich!")

        
main()