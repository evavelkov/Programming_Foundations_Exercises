def berechne_flaeche(laenge,breite): 
    #laenge = 10
    #breite = 5
    flaeche_ergebnis = laenge * breite 
    return flaeche_ergebnis 

def berechne_umfang(laenge,breite):
    umfang = 2 * (laenge + breite) 
    return umfang

def main():
    laenge = 10
    breite = 5
    flaeche_ergebnis = berechne_flaeche(laenge,breite) 
    umfang_ergebnis = berechne_umfang(laenge,breite)
    print(f"Fläche: {flaeche_ergebnis}")
    print(f"Umfang: {umfang_ergebnis}")
main()