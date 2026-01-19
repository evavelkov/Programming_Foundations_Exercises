def quadrat(zahl):
    """Berechnet das Quadrat einer Zahl.""" 
    resultat = zahl ** 2
    return resultat

def main():
    """Hauptfunktion.""" 
    x = 4
    resultat = quadrat(x)
    print(f"Das Quadrat von {x} ist {resultat}")

main()