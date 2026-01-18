anzahl = int(input("wie viele zahlen? "))
summe = 0 
for i in range(anzahl):
    zahl = float(input(f"zahl {i+1} eingeben: "))
    summe += zahl 

durchschnitt = summe / anzahl
print(durchschnitt)