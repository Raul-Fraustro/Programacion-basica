def obtener_iniciales(nombre_completo):
    palabras = nombre_completo.split()
    iniciales = "".join([palabra[0].upper() for palabra in palabras])
    return iniciales

# Ejemplo de uso
nombre = input("Ingrese un nombre completo: ")
print("Iniciales:", obtener_iniciales(nombre))