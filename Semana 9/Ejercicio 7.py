def division(a=0,b=1):
    try:   
        resultado = a/b
        return resultado
    except ZeroDivisionError:
        return print("El segundo numero tiene que ser diferente de cero")
        
a = int(input("Introduzca un numero 1: "))
b = int(input("introduzca un numero 2: "))

print(division(a,b))