"""Passwortsystem"""

passwort = "geheim123"
trials = 3 
gefunden = False

while trials > 0: 
    input_user = input("geben sie ih Passowrt ein: ").lower()
    if input_user == passwort:
        print("sie haben sich erfolgreich angemeldet!")
        gefunden = True
        break
    else: 
        trials -= 1
        if trials > 0:
            print(f"sie haben noch {trials} versuch(e)")

if not gefunden: 
    print("sie wurden gesperrt")
