#traditionelle eingabe: 
eingabe = int(input("geben sie eine Zahl ein: "))
if eingabe > 10: 
    print("diese Zahl ist grösser als 10")
else: 
    print("ist kleiner als 10")

#mit walrus-operator: 
if (eingabe := int(input("geben sie eine Zahl ein: "))) > 10:
    print("diese Zahl ist grösser als 10")
else: 
    print("ist kleiner als 10")