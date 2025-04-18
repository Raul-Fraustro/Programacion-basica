def obtener_valor(diccionario, clave):
    try:
        valor = diccionario[clave]
        return valor
    except KeyError:
        return print("Esa llave no existe")

n = int(input("Cuantos elementos quiere: "))
diccionario = {}
for i in range(n):
    llave = input("Introduzca llave: ")
    valor = input("Introduzca valor: ")
    diccionario = {llave:valor}
clave = input("Ponga la llave que ocupa: ")
print(obtener_valor(diccionario,clave))
