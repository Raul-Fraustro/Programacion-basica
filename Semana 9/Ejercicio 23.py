import re

def buscar_decimales(texto):
    patron = r'[-+]?\d*\.\d+'
    return re.findall(patron, texto)
texto = input("Introduzca texto: ")
print(buscar_decimales(texto))