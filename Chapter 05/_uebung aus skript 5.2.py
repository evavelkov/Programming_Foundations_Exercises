def teste(a, b): 
    a = a + 10
    b = b * 2
    print(f"In der Funktion: a={a}, b={b}")
    
def main(): 
    x = 5
    y = 10
    print(f"Vor dem Aufruf: x={x}, y={y}") 
    teste(x, y)
    print(f"Nach dem Aufruf: x={x}, y={y}")
main()