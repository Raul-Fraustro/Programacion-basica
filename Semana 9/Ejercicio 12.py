import math
def raiz_cuadrada(numero):
    try: 
        resultado = math.sqrt(numero)
        return resultado
    except ValueError:
        return print("El numero no puede ser un numero negativo")

numero = int(input("Introduzca un numero para sacar la raiz cuadrada: "))
print(raiz_cuadrada(numero))