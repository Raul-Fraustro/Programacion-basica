palabra = input("Introduzca palabra: \n")
vocales=0

for i in palabra:
    if i=="a" or i=="A" or i=="e" or i=="E" or i=="i" or i=="I" or i=="o" or i=="O" or i=="u" or i=="U":
        vocales+=1
print(vocales)
