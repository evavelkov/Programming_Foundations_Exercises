#autovermietungssystem, marke des autos, kennzeichen, preis pro tag, verfügbar oder nicht
#Inventarlösung

#wir öffnen eine Datei zum schreiben 
 #'w' weil wir wollen eine neue Datei erstellen
#von w auf a wechslen (nur möglich wenn es schon eine Datei gibt)

#das möchten wir in die datei hinein schreiben; siehe unten 


#das programm funktioniert noch nicht ganz 
#wenn wir oben datein offnen, müssen wir diese am schluss wieder schliessen
#weill wenn wir es nciht schliessen gehen daten verloren 
#datei.close()
#print('Auto gespeichert')

#datei.readline() -> mit dem kann man Zeilen lesen 
def autos_schreiben():
    """fügt ein neues auto hinzu"""

    try:
        
        print("\n === Neues Auto hinzufügen ===")
        model = input("Model Auto: ")
        kennzeichen = input("Kennzeichen Auto: ")
        mietpreis = input("Preis pro Tag: ")


        with open('autis.txt', 'a') as datei: #es bracuht kein x.close() mehr
                       
            datei.write(model + "\n") #eingabe kommt hier hin und es erstellt eine neue Zeile
            datei.write(kennzeichen + "\n")
            datei.write(mietpreis + "\n")
            datei.write("verfuegbar\n") 

    
        print("[OK] Auto gespeicher")
    except IOError as e:
        print(f"[FEHLER] Fehler beim Speicher: {e}")

 
def autos_anzeigen():
    """zeigt alle autos aus der Datei an"""

    try: #versuche diese datei zu öffnen und zu lesen
        datei = open('autis.txt','r')

        model = datei.readline()

        while model != '': #wenn Modell (modell iszt die erste Zeile) nicht gleich != leer ist
            kennzeichen = datei.readline()
            mietpreis = datei.readline()
            status = datei.readline() #hier sind wir bei Zeile 4 

            #asudrucken für den user 
            print(f"Model: {model.rstrip('\n')}") #rstrip / lstrip -> das eingegebene \n wird gelöscht 
            print(f"Kennzeichen: {kennzeichen.rstrip('\n')}")                                #es wird logisch gedruckt im terminal
            print(f"Mietpreis: {mietpreis.rstrip('\n')}")
            print(f"Status: {status.rstrip('\n')}")
            print('-'*40)
            
            model = datei.readline()   #holen die 5. Zeile 
        datei.close() 
    except FileNotFoundError as not_found:  #wenn es nicht geht mache das:  
        print(f"Error {not_found}")              
        print("keine Autos gefunden.")
    except Exception as e: #für alle anderem fehler
        print(f"ein Fehler ist aufgetreten {e}")
        #ggf. weiteres statement hinzufügen 


def auto_suchen(): 
    """sucht ein Auto in der Liste"""
    try:
        suchbegriff = input("\nScuhbegriff (Modell/Kennzeichen): ").lower() 

        with open('autis.txt', 'r') as datei:
            gefunden = False #FLAG wenn wir anfangen zu suchen haben wir noch nicht gefunden 

            zeile = datei.readline()

            auto_nr = 0 

            while zeile != ' ':
                auto_nr += 1
                model = zeile.rstrip("\n")
                kennzeichen = datei.readline().rstrip("\n")
                preis = datei.readline().rstrip("\n")
                status = datei.readline().rstrip("\n") #damit wir ein komplettes auto durchegeh könne müssen wir es 4 mal machen 

                if(suchbegriff in model.lower() or suchbegriff in kennzeichen.lower()):
                    if not gefunden:
                        gefunden = True #falls gefunden noch False ist, änderjetzt auf True 
                        print(" === Suchergebnisse ===")
                    print(f"Auto: {auto_nr}: {model}")
                    print(f"Kennzeichen {kennzeichen}")
                    print(f"Mietpreis: {preis}")    
                    print(f"Status: {status}")

                datei.readline()
        if not gefunden: 
            print(f"kein auto gefundenfür {suchbegriff}")
    except FileNotFoundError:
        print("keine autos vorhanden")


def zeige_menue():
    """zeigt das hauptmenu des programmes"""
    #autohinzufügen 
    #autos anzeigen
    #programm beenden
    #ungültige eingabe

    while True: 
        print('\n' + "="*50)
        print("AUTOVERMIETUNG")
        print("="*50)
        print("1. Auto hinzufügen")
        print("2. Auto anzeigen")
        print("3. Auto suchen")
        print("4. Beenden")

        wahl = input("geben sie eine Zahl ein: ")

        if wahl == 1:
            autos_schreiben()

        elif wahl == 2:
            autos_anzeigen()

        elif wahl == 3:
            auto_suchen()

        elif wahl == 4: 
            print("Auf Wiedersehen")
            break 
        else: 
            print("Eingabe ungültig!")
            

if __name__ == '__main__': #nur dann wollen wir die zwei funktionen ausführen
    zeige_menue()




