#Vamos a agarrar el archivo que se hizo en ejercicio 1
nombre_archivo = "nombres.txt"

with open(nombre_archivo, "r") as archivo:
    nombres = [linea.strip() for linea in archivo]

print("Lista de nombres:")
print(nombres)