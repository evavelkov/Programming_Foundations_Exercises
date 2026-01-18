alter = int(input("alter: "))

if alter >= 18: 
    status = "erwachsen"
else: 
    status = "minderjährig"

print(status)

#genau gleich aber in einer Zeile: 
status = "erwachsen" if alter >= 18 else "minderjährig"
print(status)
