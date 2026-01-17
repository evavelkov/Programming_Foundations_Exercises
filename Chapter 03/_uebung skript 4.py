"""Notenrechner"""

note = float(input("geben sie dir erreicht Prozentzahl ein (zwischen 0 -100): "))

if note > 0 and note <= 39:
    print("Note 1: Sehr schlecht")
elif note >= 40 and note <= 59:
    print("Note 2: Schlecht")
elif note >= 60 and note <= 69:
    print("Note 3: Ungenügend")
elif note >= 70 and note <= 79:
    print("Note 4: Genügend")
elif note >= 80 and note <= 89:
    print("Note 5: Gut")
elif note >= 90 and note <= 100:
    print("Note 6: Seh gut")
elif note < 0: 
    print("Eingabe kann nicht negativ sein")
elif note > 100: 
    print("Eingabe kann nicht grösser 100 sein")
else: 
    print("ungültige Eingabe")
