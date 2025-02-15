N = int(input("De cuantos elementos deseastu lista: \n"))

lista = []
for i in range(N):
    lista.append(int(input("Introduzca numero: ")))
band=False
while band==False:
    band=True
    for i in range(len(lista)-1):
        if lista[i]>lista[i+1]:
            aux=lista[i]
            lista[i]=lista[i+1]
            lista[i+1]=aux
            band=False
print(lista)