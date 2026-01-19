zahl = ["eva","andji","puru", "Andrea", "Marcela"]

for i in zahl: 
    print(i)

wiederholung = zahl * 2
print(wiederholung)


#der index der Position beginnt bei [0]
print(zahl[0]) # eva
print(zahl[-2]) # Andrea

print(len(zahl)) # anzahl = 5. len() zählt nicht ab 0 sondern ab 1

zahlen = [10, 20, 30, 40]
# Letztes Element sicher zugreifen: 
#letzte = zahlen[len(zahlen)] #error: len ist 4 aber es hat nur 0,1,2,3 elemente
letztes = zahlen[len(zahlen) - 1] #richtig: 4-1= 3. daher kann es gedruckt werden
print(letztes)

listeb = [i for i in range(1,6)]
print(listeb)


# 3x3-matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#martix[zeile][spalte]
print(matrix) #[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2]) #6

for zeile in matrix: #[1, 2, 3], [4, 5, 6], ....
    for zahl in zeile: #hier nimmt es nur die einzelne Zahl in der Liste "1", "2", "3"
        print(zahl, end=" ") #1 2 3 4 5 6 7 8 9 gibt Zhalen aus aber endet mit leerzeichen statt mit einem \n
    print() #1 2 3
            #4 5 6 
            #7 8 9

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"matrix[{i}][{j}] = {matrix [i][j]}")

for i in range(len(matrix)):
    print([i])
    for j in range(len(matrix[i])):
        print(j)


