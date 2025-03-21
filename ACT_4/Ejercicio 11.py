def generar_matriz(n, m):
    matriz = [[(i + j) % 2 for j in range(m)] for i in range(n)]
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(map(str, fila)))

n = int(input("Ingrese el número de filas: "))
m = int(input("Ingrese el número de columnas: "))

matriz = generar_matriz(n, m)
imprimir_matriz(matriz)
