n=int(input("Cuantas numeros quiere: "))

lista=list()
for i in range(n):
    lista.append(input(f"{i+1}. Introduzca Numero:"))
    
nombre_archivo = "nombres.txt"
with open(nombre_archivo, "w") as archivo:
    for numero in lista:
        archivo.write(numero + "\n")
   
with open(nombre_archivo, "r") as archivo:
    suma = []
    lineas = nombre_archivo
    for linea in archivo:
        numero = int(linea.strip())
        suma.append(numero)
suma_total = sum(suma)

print(suma_total)