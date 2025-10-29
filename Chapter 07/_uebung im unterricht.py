

z = [ 2, 3, 4]
zweite_ref_auf_z = 2 #jede art von änderung in z, führt zu einer änderung in zweite_ref_auf_z auswirkung haben


z.append(5)
print(z)
print(zweite_ref_auf_z) #ist aber keine kopie von der ersten liste sonder nur eine referenz (denke an referenz in MicroStation)


val1 = 3
val2 = val1 #kopie 

# kopie von listen (= erzeugt keien kopie)¨
z_kopie = z.copy()
# führt zu m gleichern ergebnis wie ein manuelles kpieren
z_kopie_2 = [] 
for e in z: 
    z_kopie_2.append(e)
#füht zum gleicher ergebnis 

z_kopie_3 = z[:] # slcie von 0 bis len(z)
#führt zum gleichen wie

z_kopie_4 = list(z) 

# zwei dimensionale listen 

matrix = [ [1, 2, 3,], [4, 5, 6], [7,8,9,]]
print(matrix) 

zeile_1 = matrix[0] #die erste stelle in der liste aufrufen : liste [1, 2, 3]
print(zeile_1)

wert_1= matrix [0][1][0]
print(wert_1) 


# wie müsste iene schaleife ausseehen die ienze ganze index struktur drchläuft 
for zeile in matrix:
    for element in zeile:
        print(element, end= ' ') #var die durhc dielsiten durhcläuf t


for i in range(0, 2) # = erhalten eine lsite die besteht aus den werten [0 , 1]

#for schleife in rage i
# inenrhalb diese forschleife in rage j um den inhalt der playlist darzustellen (siehe bikd auf dem handy) 