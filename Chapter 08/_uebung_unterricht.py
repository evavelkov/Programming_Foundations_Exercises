lst = [2, 3, 4]
#Zu Beachten: 1. Datentypen müssen zu Strings konvertiert werden,
# 2. Exceütopms gemäss Dokumentation von "open" verwenden
try:
    with open("liste.txt", "w") as datei:
        lst_str = [zahl for zahl in lst] #wir benätigen ["2", "3", "4"]
        #langschreibweise:
       # for zahl in lst:
            #lst_str.append( str(zahl))
            #Schreibe Zeile für Zeile in die Datei
        for lst_element in lst_str:
            datei.write(lst_element + "\n")
except FileNotFoundError as e:
    print("keien rechte für eine Schleife")
except PermissionError as e:
    print("keine Reichte für diesen ordner")
except IsADirectoryError as e: 
    print("ein Ordneer mit gleichen Namen existiert")
except OSError as E: 
    print("ein betriebfehelr ist passiert")

liste_eingelesen = []
with open ("liste.txt", "r") as datei: 
    liste_eingelesen = datei.readlines() #liest zeiel für zeiel, aber alle zeilen 
    liste_eingelesen = [int(zahl) for zahl in liste_eingelesen  ]   #konvertieren von str nach int
                                                                    #[ "2", "3", "4"] => [2,3,4]
#lange schreibweise:
#liste_eingelesen_str = []
#for zahl in liste_eingelesen:
#    liste_eingelesen_str.append(int(zahl))
#liste_eingelesen = liste_eingelesen_str

print(liste_eingelesen)

#liste mit verschieden typen
lst_liste = [22, "a concert", "eine Beschreibung ...", 
             22, "the show", "eine Begrüssung ..."]

#ausnahme: eindeutigkeit stets ID (Typ Int), name  typt str, beschreibung (typ str) 
lst_listen_str = []
for i in range ( 0, len(lst_liste)): #konvertieren 
    rest = (i+1) % 3 #modulu 3 weil wir den rest berechen. den rest weil das sind die intialisten den liste
    if rest == 1: #
        #erster wert
        lst_listen_str.append(str(lst_liste[i]))


#alternativlösung 1: zwidimensionale liste

#alternativlösung 2: versuch konvertieren, bei exception abbruch der konvertierung
#funktioniert immer und funktioniert automatisch (richtig)
#nachteil: wenn das format ändert, kann man es leicht anpassen.. kann aber ausversehen ändern und dann funktioniert es nicht mehr

#alternativlösung 3: dictionaries 


#kapitel 8 
