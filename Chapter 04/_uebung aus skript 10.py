"""Zinseszinz-Rechner"""

jahreszinssatz = 0.0
gesamtzuwachs = 0

print("=== ZINSESZINS RECHNER ==")

anfangskapital = float(input("Was ist dein Anfangskapital? "))
while anfangskapital <= 0: 
    print("Anfangskapital kann nicht negativ sein!")
    anfangskapital = float(input("Was ist dein Anfangskapital? "))

prozent = float(input("Jahreszinssatz (%): "))
while prozent <= 0: 
    print("Zinssatz kann nicht negativ sein!")
    prozent = float(input("Jahreszinssatz (%): "))

laufzeit= int(input("Wie viele Jahre? "))
while laufzeit <= 0:
    print("Laufzeit muss minimum 1 Jahr gehen.")
    laufzeit= int(input("Wie viele Jahre? "))

jahreszinssatz = prozent / 100 

kapital = anfangskapital # end-kapital = Kapital * (1+Zinssatz)

for i in range(1, laufzeit+1): 
    kapital = kapital * (1 + jahreszinssatz)
    zuwachs = kapital - anfangskapital
    gesamtzuwachs += zuwachs
    print(f"dein Kapital ist: {kapital:.2f}chf mit einem Zuwachs von {zuwachs:.2f}chf im Jahr {i}.")
print(f"dein ZUwachs ist: {gesamtzuwachs:.2f}chf.")
