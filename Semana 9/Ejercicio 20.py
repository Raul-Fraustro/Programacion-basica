import re 
def numero_de_tarjeta(num_tarjeta):
    patron = r"\d{4}+-+\d{4}+-+\d{4}+-+\d{4}"
    return re.match(patron, num_tarjeta) is not None
numero_tarjeta = input("Introduzca numero de tarjeta: ")
print(numero_de_tarjeta(numero_tarjeta))