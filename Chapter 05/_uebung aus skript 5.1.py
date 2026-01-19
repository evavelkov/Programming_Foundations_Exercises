def main():
    wert1 = float(input("geben sie Wert 1 ein: "))
    wert2 = float(input("geben sie Wert 2 ein: "))
    wert3 = float(input("geben sie Wert 3 ein: "))
    durchschnitt(wert1, wert2, wert3)
    
def durchschnitt(x,y,z):
    while x == None: 
        x = 0
    while y == None: 
        y = 0
    while z == None: 
        z = 0
    durchschnitt = (x+y+z) / 3
    print(f"der Durchschnitt it: {durchschnitt}")

main()