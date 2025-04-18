
def convertir_a_entero(cadena):
    try:
        numero = int(cadena)
        return numero
    except ValueError:
        return("La cifra tiene una letra: ")


print(convertir_a_entero(input("Introduzca numero: ")))