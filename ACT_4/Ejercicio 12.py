def capturar_matriz():
    matriz = []
    print("Ingrese los elementos de la matriz 3x3, fila por fila:")
    for _ in range(3):
        fila = list(map(int, input().split()))
        matriz.append(fila)
    return matriz

def sumar_matrices(matriz1, matriz2):
    return [[matriz1[i][j] + matriz2[i][j] for j in range(3)] for i in range(3)]

print("Captura de la primera matriz:")
matriz1 = capturar_matriz()
print("Captura de la segunda matriz:")
matriz2 = capturar_matriz()

resultado = sumar_matrices(matriz1, matriz2)

print("Resultado de la suma de matrices:", resultado)

