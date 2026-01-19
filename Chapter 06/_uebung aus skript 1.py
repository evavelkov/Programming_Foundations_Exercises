#Notenschreiber
def main(): 
    name = input("geben sie den Namen des Schülers ein: ")
    #eigentlich wollten sie dass der Name das Schülers ebenfalls gedruckt wird, und nciht als Datei erstellt wird. 
    #code ist aber prinzipiel richtig. 
    dateiname = name + '.txt'

    note1 = float(input("Erste Note des Schülers: "))
    note2 = float(input("Zweite Note des Schülers: "))
    note3 = float(input("Dritte Note des Schülers: "))
    noten_schreiben(dateiname, note1, note2, note3)

def noten_schreiben(dateiname, note1, note2, note3): 
    try: 
        with open(dateiname, 'w') as datei_noten: 
            datei_noten.write(str(note1) + '\n')
            datei_noten.write(str(note2) + '\n')
            datei_noten.write(str(note3) + '\n')

    except Exception as e: 
        print(f"Fehler gefunden {e}")
    else: 
        print("Datei wurde erfolgreich erstellt.")

if __name__ == '__main__':
    main()