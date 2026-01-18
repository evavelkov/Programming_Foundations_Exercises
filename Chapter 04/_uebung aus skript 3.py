"""rechner fakultät von eingabe benutzer"""
"""z.B. 5! = 5 * 4 * 3 * 2 * 1 = 120"""

loesung = 1 #0 geht nicht da es alles * 0 rechnet = 0. none geht nicht weil es eine Zahl benötigt!
zahl = int(input("geben sie eine zahl ein: "))

for i in range(1, zahl+1): 
    loesung *= i
print(f"das Fakultät von {zahl} ist {loesung}.")