def main(): 
    while True: 
        eingabe = input("Wählen sie zwischen 1 und 2: ")
        
        if eingabe == "1": 
            willkommen()

        elif eingabe == "2":
            abschied()
        
        else: 
            print("ungültige Eingabe.")
            eingabe = input("Wählen sie zwischen 1 und 2: ")

def willkommen():
    print("Hi, Wilkommen zu meinem ersten Programm!")
    main()

def abschied(): 
    print("Danke und aufwiedershen!")

main()