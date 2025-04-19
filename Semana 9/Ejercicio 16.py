import re
def buscar_numero(texto):
    patron = r'\+\d{2}[-\s]\d{4}[-\s]\d{4}'
    return re.findall(patron, texto)
texto = input("Introduzca texto: ")

telefonos_encontrados = buscar_numero(texto)

if telefonos_encontrados:
    print("Números encontrados:")
    for telefono in telefonos_encontrados:
        print("-", telefono)
else:
    print("No se encontraron números de teléfono con el formato esperado.")