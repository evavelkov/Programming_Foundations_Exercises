def oeffne_liste_noten(): 
    """zeigt die noten welche angegeben wurden in der Liste"""
    try: 
        with open ('noten.txt', 'r') as datei:
            name = datei.readline()

            while name != '': 
                note1 = float(datei.readline())
                note2 = float(datei.readline())
                note3 = float(datei.readline()) #hier sind wir bei der 4. Zeile 

                durchschnitt = (note1 + note2 + note3)/3

                #ausdrucken für den user
                print(f"Name: {name.rstrip('\n')}")
                print(f"Note 1: {note1}")
                print(f"Note 2: {note2}")
                print(f"Note 3: {note3}")
                print(f"Durchschnitt von {name.rstrip('\n')} ist: {durchschnitt:.2f}")
                print('-'*50)


                name = datei.readline() #hole 5. Zeile; Schleife geht weiter

    except FileNotFoundError as not_found:
        print(f"Error {not_found}")
        print("Es wurden keien Noten gefunden")
    except Exception as e: 
        print(f"es wurde ein Fehler gefunden: {e}")
    finally:
        print("Vorgang wurde abgeschlossen")

if __name__ == '__main__':
    oeffne_liste_noten()