num = int(input("De cuantos elementos desea la lista:\n"))
lista = []
for i in range(num):
    lista.append(int(input("Introduzca nu numero: ")))
M = lista[1]
m = lista[1]
for i in range(num):
    if lista[i]<m:
        m = lista[i]
    elif lista[i]>M:
        M = lista[i]
print(f"Numeor mayor: {M}",f"Numeor menor: {m}")
