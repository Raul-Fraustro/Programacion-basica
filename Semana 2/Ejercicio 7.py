num = int(input("De cuantos elemento desea la lista: \n"))
lista = []
suma=0
for i in range(num):
    lista.append(int(input("Introducza numero:")))
    suma+=lista[i]
print(suma)