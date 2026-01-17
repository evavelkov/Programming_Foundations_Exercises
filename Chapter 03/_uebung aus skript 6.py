"""Ampel-Steuerung"""

uhrzeit = float(input("Was ist die aktuelle Uhrzeit?: "))
autos = int(input("Anzahl wartende Autos vor dedr Ampel: "))
feiertag = input("ist es ein Feiertrag?(j/n): ").lower() == "j"
notfall = input("ist es ein Notfall?(j/n): ").lower() == "j"

if uhrzeit < 6 and uhrzeit >= 22:
    ampelstatus = "dauergelb"
    print("die Ampel ist dauergelb, daher haben sie freie fahrt.")
elif notfall == True: 
    print("die Ampel wird auf grün gestellt für 60 Sekunden.")
else:
    print("die Wartezeit und der Ampelstatus ist regulär")




