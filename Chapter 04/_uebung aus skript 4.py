"""Notenvalidierung"""

note = int(input("geben sie eine Note (1-6) ein: "))

while note < 1 or note > 6:
    print("ungültige Auswahl")
    note = int(input("geben sie eine Note (1-6) ein: "))

print(f"sie haben die Note {note} gewählt.")