def main(): 
    with open('MAs.txt', 'r') as datei: 
            while datei != " ": 
                name = datei.readline().rstrip("\n")
                pnummer = datei.readline().rstrip("\n")
                abteilung = datei.readline().rstrip("\n")
                stundenlohn = datei.readline().rstrip("\n")

                print(name)
                print(pnummer)
                print(abteilung)
                print(stundenlohn)
                print("Verarbeitung abgeschlossen")


main()