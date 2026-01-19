def test1():
    wert = 100
    print(f"test1: wert = {wert}")
def test2():
    wert = 200
    print(f"test2: wert = {wert}")
def main():
    wert = 300
    print(f"main: wert = {wert}") 
    test1()
    test2()
    print(f"main: wert = {wert}")
main()