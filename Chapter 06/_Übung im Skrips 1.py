def noten_registrieren():
    """die Lehrperson muss Namen und drei Noten regisitieren"""
    try: 
        name= input("Name des Schülers: \n")
        note1 = float(input("Erste Note: \n"))
        note2 = float(input("Zweite Note: \n"))
        note3 = float(input("Dritte Note: \n"))

        with open('noten.txt', 'a') as datei: 
            datei.write(name + "\n")
            datei.write(str(note1) + "\n")
            datei.write(str(note2) + "\n")
            datei.write(str(note3) + "\n")

        print("Name und Note des Schülers wurde registiriert")

    except IOError as e:
        print(f"Fehler beim Schreiben der Datei: {e}")
    except ValueError:
        print("Fehler: Ungültig Eingabe für Noten.")


if __name__ == '__main__':
    noten_registrieren()