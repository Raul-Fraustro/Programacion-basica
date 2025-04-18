def obtener_elemento(lista, indice):
    try:
        elemento = lista[indice]
        return elemento
    except IndexError:
        return print("El indice se encuenta fuera de rango")
lista = []
n = int(input("Cuantos elemntos quiere en la lista: "))
for i in range(n):
    lista.append(input("Introduzca elemento: "))
indice = int(input("Que numero de elemento desea: "))

print(obtener_elemento(lista,indice))
    