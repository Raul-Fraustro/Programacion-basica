import re

def validar_usuario(nombre_usuario):
    patron = r'^[a-zA-Z0-9_]{3,16}$'
    return re.match(patron, nombre_usuario) is not None

nombre_usuario = input("Introduzca nombre de usuario de 3 a 16 caracteres: ")
print(validar_usuario(nombre_usuario))