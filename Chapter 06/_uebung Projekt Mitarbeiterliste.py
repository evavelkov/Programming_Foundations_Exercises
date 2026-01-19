def main(): 
    with open('_MAs.txt', 'r') as datei: 
            name = datei.readline().rstrip('\n')

            while name != "": 
                    nummer = datei.readline().rstrip('\n')
                    abteilung = datei.readline().rstrip('\n')
                    lohn = datei.readline().rstrip('\n')

                    print(f"\nName: {name}")
                    print(f"Personalnummer: {nummer}")
                    print(f"Abteilung: {abteilung}")
                    print(f"Stundenlohn: {lohn}")

                    name = datei.readline().rstrip('\n')

main()