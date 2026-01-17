preis = 1.65 #chf/Liter

print(" === BENZINKOSTEN-RECHNER ===")
strecke = float(input("geben sie bitte ihre Gefahrene Strecke im km ein: "))
verbrauch = float(input("Verbrauch Liter/100km: "))

menge_noetig =  strecke / 100 * verbrauch 
total_kosten = menge_noetig * preis 

print(f"GESAMTKOSTEN: {total_kosten:.2f}chf")

