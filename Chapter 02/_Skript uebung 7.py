steuer = 0.19
trinkgeld = 0.18
1 = 'margherita'
preis1 = 20

2 = 'capriccoiosa'
preis2 = 23

3 = 'mairinara'
preis3 = 23

gericht_wahl = int(input("Welche Pizza möchtes du wählen? (1,2,3): "))
print(30*"=")
print("Restaurant Rechnung")
print(30*"=")
print("Restaurant : Pizza Place")
if gericht_wahl == 1:
    print(f"Gericht: {1}")
    steuerpreis1 = print(f"Steuer(19%): {preis1 * steuer} chf")
    zsum1 = print(f"zwischensumme: {steuerpreis1 + preis1} chf")
    trinkgeld1 = print(f"Trinkgeld(18%): {zsum1 * trinkgeld}")