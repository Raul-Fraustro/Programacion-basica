def ordenamiento(palabras):
    return sorted(palabras,key=len )

n = int(input("Cuantas palabras quieres: "))
palabras = list()
for i in range(n):
    palabras.append(input("Introduzca palabras: "))
resultado = ordenamiento(palabras)
print(resultado)
