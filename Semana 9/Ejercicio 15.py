import re 
def validar_correo(correo):
    patron = r"^[a-zA-Z]+@[a-zA-z]+\.[a-zA-z]{3}$"
    return re.match(patron, correo) is not None
correo = (input("Introduzca correo: "))
print(validar_correo(correo))