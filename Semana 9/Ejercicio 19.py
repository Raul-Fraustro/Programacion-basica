import re
def buscar_mayusculas(texto):
    patron = r"\b[A-Z][a-zA-Z]*\b"
    return re.findall(patron, texto)

texto = input("Introduzca texto: ")
print(buscar_mayusculas(texto))